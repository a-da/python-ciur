"""
ciur external dsl

FIXME: using russian characters in pyparsing

>>> import pprint
>>> bnf = _get_bnf()

example.com.doctest
===================
>>> rules = '''
... root `/html/body` +1
...    name `.//h1/text()` +1
...    paragrapth `.//p/text()` +1
... '''

>>> pprint.pprint(get_list(rules))
[['root',
  'xpath',
  '/html/body',
  ['+1'],
  [['name', 'xpath', './/h1/text()', ['+1']],
   ['paragrapth', 'xpath', './/p/text()', ['+1']]]]]

import.io_jobs.doctest
======================
>>> rules = '''
... root `/jobs/job` +
...
...     title `./title/text()` +
...     url `./url/text()` +1
...     location `.` *
...         country `./country/text()` +1
...         city `./city/text()` +1
...         zip `./postalcode/text()` *1
... '''
>>> pprint.pprint(get_list(rules))
[['root',
  'xpath',
  '/jobs/job',
  ['+'],
  [['title', 'xpath', './title/text()', ['+']],
   ['url', 'xpath', './url/text()', ['+1']],
   ['location',
    'xpath',
    '.',
    ['*'],
    [['country', 'xpath', './country/text()', ['+1']],
     ['city', 'xpath', './city/text()', ['+1']],
     ['zip', 'xpath', './postalcode/text()', ['*1']]]]]]]

>>> print to_json(rules)  # doctest: +NORMALIZE_WHITESPACE
[
    {
        "name": "root",
        "selector_type": "xpath",
        "selector": "/jobs/job",
        "type_list": [
            "+"
        ],
        "rule": [
            {
                "name": "title",
                "selector_type": "xpath",
                "selector": "./title/text()",
                "type_list": [
                    "+"
                ]
            },
            {
                "name": "url",
                "selector_type": "xpath",
                "selector": "./url/text()",
                "type_list": [
                    "+1"
                ]
            },
            {
                "name": "location",
                "selector_type": "xpath",
                "selector": ".",
                "type_list": [
                    "*"
                ],
                "rule": [
                    {
                        "name": "country",
                        "selector_type": "xpath",
                        "selector": "./country/text()",
                        "type_list": [
                            "+1"
                        ]
                    },
                    {
                        "name": "city",
                        "selector_type": "xpath",
                        "selector": "./city/text()",
                        "type_list": [
                            "+1"
                        ]
                    },
                    {
                        "name": "zip",
                        "selector_type": "xpath",
                        "selector": "./postalcode/text()",
                        "type_list": [
                            "*1"
                        ]
                    }
                ]
            }
        ]
    }
]

scrapy.org_support.doctest
==========================
>>> rules = '''
... company_list `.//div[@class='company-box']` +
...     name `.//span[@class='highlight']/text()` +
...     company_url `./a/@href` +1
...     blog_url `./p/a/@href` *
...     logo `./a/img/@src` +
... '''

>>> pprint.pprint(get_list(rules))
[['company_list',
  'xpath',
  ".//div[@class='company-box']",
  ['+'],
  [['name', 'xpath', ".//span[@class='highlight']/text()", ['+']],
   ['company_url', 'xpath', './a/@href', ['+1']],
   ['blog_url', 'xpath', './p/a/@href', ['*']],
   ['logo', 'xpath', './a/img/@src', ['+']]]]]

>>> print to_json(rules)  # doctest: +NORMALIZE_WHITESPACE
[
    {
        "name": "company_list",
        "selector_type": "xpath",
        "selector": ".//div[@class='company-box']",
        "type_list": [
            "+"
        ],
        "rule": [
            {
                "name": "name",
                "selector_type": "xpath",
                "selector": ".//span[@class='highlight']/text()",
                "type_list": [
                    "+"
                ]
            },
            {
                "name": "company_url",
                "selector_type": "xpath",
                "selector": "./a/@href",
                "type_list": [
                    "+1"
                ]
            },
            {
                "name": "blog_url",
                "selector_type": "xpath",
                "selector": "./p/a/@href",
                "type_list": [
                    "*"
                ]
            },
            {
                "name": "logo",
                "selector_type": "xpath",
                "selector": "./a/img/@src",
                "type_list": [
                    "+"
                ]
            }
        ]
    }
]
"""

from collections import OrderedDict
import os
import re

from pyparsing import (
    col,
    lineEnd,
    empty,
    alphas,
    alphanums,
    printables,
    pythonStyleComment,
    delimitedList,
    QuotedString, oneOf)
from pyparsing import (
    ParseFatalException,
    ParseException,
    FollowedBy,
    Word,
    Regex,
    Optional,
    Forward,
    OneOrMore,
    Group,
    Literal,
    Suppress,
    ParseBaseException,
    ZeroOrMore,
    Or
)
from lxml import etree
from ciur import pretty_json, CiurException
from ciur import cast


class ParseExceptionInCiurFile(ParseBaseException):
    def __init__(self, file_string, file_name, p):
        ParseBaseException.__init__(self, p.pstr, p.loc, p.msg, p.parserElement)
        self._file_string = file_string.splitlines()
        self._file_name = None if not file_name else os.path.abspath(file_name)

    def __str__(self):
        s = "|from file `%s`" % self._file_name if self._file_name else "from string"

        line = "%s" % self.lineno

        return "%s,\n    %s \n    |%s: %s\n    %s^" % (
            ParseBaseException.__str__(self),
            s,
            line,
            self._file_string[self.lineno - 1],
            " " * (self.col + 1 + len(line))
        )


_indent_stack = [1]


def _check_peer_indent(s, l, tock):
    cur_col = col(l, s)
    if cur_col != _indent_stack[-1]:
        if (not _indent_stack) or cur_col > _indent_stack[-1]:
            raise ParseFatalException(s, l, "illegal nesting")
        raise ParseException(s, l, "not a peer entry ????")


def _check_sub_indent(s, loc, tock):
    cur_col = col(loc, s)
    if cur_col > _indent_stack[-1]:
        _indent_stack.append(cur_col)
    else:
        raise ParseException(s, loc, "not a subentry")


def _check_unindent(s, loc):
    if loc >= len(s):
        return

    cur_col = col(loc, s)
    if not(cur_col < _indent_stack[-1] and cur_col <= _indent_stack[-2]):
        raise ParseException(s, loc, "not an unindent")


def do_unindent():
    _indent_stack.pop()


def validate_identifier(s, loc, tock):
    identifier = tock[0]
    if identifier.endswith(":"):
        raise ParseFatalException(
            s,
            loc + len(identifier),
            "validate_identifier-> not allowed `:` delimiter symbol at the end"
        )

    if identifier.startswith(":"):
        raise ParseFatalException(
            s,
            loc + 1,
            "validate_identifier-> not allowed `:` delimiter symbol at the begin"
        )

    index = identifier.find("::")
    if index >= 0:
        raise ParseFatalException(
            s,
            loc + index + 1,
            "validate_identifier-> duplicate `:` delimiter"
        )


def type_list_validation(s, loc, expr, err):
    """
    add more explicit error handling in case if bnf fail
    """
    raise ParseFatalException(s, loc, "type_list_validation->%s" % err)


def _get_bnf(namespace=None):
    def validate_xpath(s, loc, tock):
        """
        :type tock: list of str
        """
        xpath_ = tock[0]
        try:
            if re.search("number\(.*\)", s):
                import sys
                sys.stderr.write(
                    "[WARNING] use `float` from type_list instead of `number` from xpath, "
                    "because number lies see "
                    "http://stackoverflow.com/questions/33789196/is-xpath-number-function-lies\n")

            context = etree.fromstring("<root></root>")
            context.xpath(xpath_, namespaces=namespace)
            # XPATH_EVALUATOR(xpath_, namespaces=namespace)
        except etree.XPathEvalError, e:
            raise ParseFatalException(s, loc, "validate_xpath->%s" % e)
        pass

    grave = Suppress("`")
    indent = lineEnd.suppress() + empty + empty.copy().setParseAction(_check_sub_indent)
    undent = FollowedBy(empty).setParseAction(_check_unindent).setParseAction(do_unindent)

    # TODO: describe ":" variable comprehention
    # <url> ./url str +1 => label of rule
    identifier = Word(alphas, alphanums + "_:").addParseAction(validate_identifier)

    # url <./url> str +1 => xpath query
    #xpath = grave + Word(printables + " ", excludeChars="`").addParseAction(validate_xpath) + grave
    xpath = Optional(oneOf("xpath css css/"), default="xpath") + QuotedString(quoteChar="`")

    casting_functions_args = Optional(Suppress("(") + delimitedList(identifier) + Suppress(")"))

    casting_functions = Or(
        Group(Literal(i[:-1]) + casting_functions_args) for i in dir(cast)
        if i.endswith("_") and not i.startswith("__")
    )

    type_list = Group(
        ZeroOrMore(casting_functions) +  # url ./url <str> +1 => functions chains for transformation
        Regex("[\+*]\d*")  # url ./url str <+1>  => size match: + mandatory, * optional, \d+ exact len
    ).setFailAction(type_list_validation)

    rule = (identifier + xpath + type_list)  # <url ./url str +1> => rule line

    stmt = Forward().setParseAction(_check_peer_indent)
    bnf = OneOrMore(stmt)

    children = Group(indent + bnf + undent).ignore(pythonStyleComment)
    stmt << Group(rule + Optional(children))  # check for children

    return bnf


def get_list(rules, namespace=None):
    """
    :param rules: file or basestring
    :return:
    """
    assert isinstance(rules, (file, basestring))

    file_name = None
    if isinstance(rules, file):
        file_name = rules.name
        rules = rules.read()

    if not re.search("\n\s*$", rules):
        raise CiurException("no new line at the end of file", {"file_name": os.path.abspath(file_name)})

    try:
        bnf = _get_bnf(namespace=namespace)
        parse_tree = bnf.parseString(rules, parseAll=True)
    except ParseBaseException, e:
        raise ParseExceptionInCiurFile(rules, file_name, e)

    return parse_tree.asList()


def _to_dict(rule_list):
    rule_list_out = []

    for rule_i in rule_list:
        d = OrderedDict()
        d["name"] = rule_i[0]
        d["selector_type"] = rule_i[1]
        d["selector"] = rule_i[2]
        d["type_list"] = rule_i[3]
        if len(rule_i) == 5:
            d["rule"] = _to_dict(rule_i[4])

        rule_list_out.append(d)

    return rule_list_out


def to_json(rules):
    list_ = get_list(rules)

    data = _to_dict(list_)

    return pretty_json(data)


def to_dict(rules, namespace=None):
    list_ = get_list(rules, namespace=namespace)

    data = _to_dict(list_)

    return data


# ------------
# CONSTANTS
# ------------

# noinspection PyUnresolvedReferences
import lxml_xpath2  # load namespace function in lxml.etree
