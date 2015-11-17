# -*- coding: utf-8 -*-
"""
ciur external dsl

>>> import pprint
>>> bnf = _get_bnf()

example.com.doctest
===================
>>> rules = '''
... root `/html/body` +1
...    name `.//h1` str +1
...    paragrapth `.//p` str +1
... '''

>>> pprint.pprint(get_list(rules))
[['root',
  '/html/body',
  ['+1'],
  [['name', './/h1', ['str', '+1']], ['paragrapth', './/p', ['str', '+1']]]]]

import.io_jobs.doctest
======================
>>> rules = '''
... root `/jobs/job` +
...
...     title `./title` str +
...     url `./url` str +1
...     location `.` *
...         country `./country` str +1
...         city `./city` str +1
...         zip `./postalcode` str *1
... '''
>>> pprint.pprint(get_list(rules))
[['root',
  '/jobs/job',
  ['+'],
  [['title', './title', ['str', '+']],
   ['url', './url', ['str', '+1']],
   ['location',
    '.',
    ['*'],
    [['country', './country', ['str', '+1']],
     ['city', './city', ['str', '+1']],
     ['zip', './postalcode', ['str', '*1']]]]]]]

>>> print to_json(rules)  # doctest: +NORMALIZE_WHITESPACE
[
    {
        "name": "root",
        "xpath": "/jobs/job",
        "type_list": [
            "+"
        ],
        "rule": [
            {
                "name": "title",
                "xpath": "./title",
                "type_list": [
                    "str",
                    "+"
                ]
            },
            {
                "name": "url",
                "xpath": "./url",
                "type_list": [
                    "str",
                    "+1"
                ]
            },
            {
                "name": "location",
                "xpath": ".",
                "type_list": [
                    "*"
                ],
                "rule": [
                    {
                        "name": "country",
                        "xpath": "./country",
                        "type_list": [
                            "str",
                            "+1"
                        ]
                    },
                    {
                        "name": "city",
                        "xpath": "./city",
                        "type_list": [
                            "str",
                            "+1"
                        ]
                    },
                    {
                        "name": "zip",
                        "xpath": "./postalcode",
                        "type_list": [
                            "str",
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
...     name `.//span[@class='highlight']` str +
...     company_url `./a/@href` str +1
...     blog_url `./p/a/@href` str *
...     logo `./a/img/@src` str +
... '''

>>> pprint.pprint(get_list(rules))
[['company_list',
  ".//div[@class='company-box']",
  ['+'],
  [['name', ".//span[@class='highlight']", ['str', '+']],
   ['company_url', './a/@href', ['str', '+1']],
   ['blog_url', './p/a/@href', ['str', '*']],
   ['logo', './a/img/@src', ['str', '+']]]]]

>>> print to_json(rules)  # doctest: +NORMALIZE_WHITESPACE
[
    {
        "name": "company_list",
        "xpath": ".//div[@class='company-box']",
        "type_list": [
            "+"
        ],
        "rule": [
            {
                "name": "name",
                "xpath": ".//span[@class='highlight']",
                "type_list": [
                    "str",
                    "+"
                ]
            },
            {
                "name": "company_url",
                "xpath": "./a/@href",
                "type_list": [
                    "str",
                    "+1"
                ]
            },
            {
                "name": "blog_url",
                "xpath": "./p/a/@href",
                "type_list": [
                    "str",
                    "*"
                ]
            },
            {
                "name": "logo",
                "xpath": "./a/img/@src",
                "type_list": [
                    "str",
                    "+"
                ]
            }
        ]
    }
]

>>> print to_json(rules)  # doctest: +NORMALIZE_WHITESPACE
[
    {
        "name": "company_list",
        "xpath": ".//div[@class='company-box']",
        "type_list": [
            "+"
        ],
        "rule": [
            {
                "name": "name",
                "xpath": ".//span[@class='highlight']",
                "type_list": [
                    "str",
                    "+"
                ]
            },
            {
                "name": "company_url",
                "xpath": "./a/@href",
                "type_list": [
                    "str",
                    "+1"
                ]
            },
            {
                "name": "blog_url",
                "xpath": "./p/a/@href",
                "type_list": [
                    "str",
                    "*"
                ]
            },
            {
                "name": "logo",
                "xpath": "./a/img/@src",
                "type_list": [
                    "str",
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

import pyparsing
from pyparsing import (
    col,
    lineEnd,
    empty,
    alphas,
    alphanums,
    printables,
    pythonStyleComment,
    ParseBaseException, ZeroOrMore
)

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
    Suppress
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


def validate_xpath(s, loc, tock):
    """
    :type tock: list of str
    """
    try:
        XPATH_EVALUATOR(tock[0])
        i = 10
        #TEST_DOM_SAMPLE.xpath(tock[0])
    except etree.XPathEvalError, e:
        raise ParseFatalException(s, loc, "validate_xpath->%s" % e)


def _get_bnf():
    grave = Suppress("`")
    indent = lineEnd.suppress() + empty + empty.copy().setParseAction(_check_sub_indent)
    undent = FollowedBy(empty).setParseAction(_check_unindent).setParseAction(do_unindent)

    identifier = Word(alphas, alphanums + "_")  # <url> ./url str +1 => label of rule

    # url <./url> str +1 => xpath query
    xpath = grave + Word(printables + u" şăţ", excludeChars="`").addParseAction(validate_xpath) + grave

    casting_functions = pyparsing.Or(
        Literal(i[:-1]) for i in dir(cast) if i.endswith("_") and not i.startswith("__")

    )

    type_list = Group(
        ZeroOrMore(casting_functions) +  # url ./url <str> +1 => functions chains for transformation
        Regex("[\+*]\d*")   # url ./url str <+1>  => size match: + mandatory, * optional, \d+ exact len
    )

    rule = (identifier + xpath + type_list)  # <url ./url str +1> => rule line

    stmt = Forward().setParseAction(_check_peer_indent)
    bnf = OneOrMore(stmt)

    children = Group(indent + bnf + undent).ignore(pythonStyleComment)
    stmt << Group(rule + Optional(children))  # check for children

    return bnf


def get_list(rules):
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
        parse_tree = BNF.parseString(rules, parseAll=True)
    except ParseBaseException, e:
        raise ParseExceptionInCiurFile(rules, file_name, e)

    return parse_tree.asList()


def _to_dict(rule_list):
    rule_list_out = []

    for rule_i in rule_list:
        d = OrderedDict()
        d["name"] = rule_i[0]
        d["xpath"] = rule_i[1]
        d["type_list"] = rule_i[2]
        if len(rule_i) == 4:
            d["rule"] = _to_dict(rule_i[3])

        rule_list_out.append(d)

    return rule_list_out


def to_json(rules):
    list_ = get_list(rules)

    data = _to_dict(list_)

    return pretty_json(data)


def to_dict(rules):
    list_ = get_list(rules)

    data = _to_dict(list_)

    return data


def matches(context, text, regex):
    """
    The function returns true if a matches the regular expression supplied as $pattern as influenced by the value
    of $flags, if present; otherwise, it returns false.

    see more http://www.w3.org/TR/xpath-functions/#func-matches

    :param context: DOM context
    :param text: input as string
    :param regex:
    :return:
    """
    assert isinstance(text, list) and len(text) == 1

    import re
    return bool(re.search(regex, text[0]))

def matches(context, text, regex):
    """
    The function returns true if a matches the regular expression supplied as $pattern as influenced by the value
    of $flags, if present; otherwise, it returns false.

    see more http://www.w3.org/TR/xpath-functions/#func-matches

    :param context: DOM context
    :param text: input as string
    :param regex:
    :return:
    """
    assert isinstance(text, list) and len(text) == 1

    import re
    return bool(re.search(regex, text[0]))

ns = etree.FunctionNamespace(None)
ns['matches'] = matches


# ------------
# CONSTANTS
# ------------
BNF = _get_bnf()

import lxml_xpath2
XPATH_EVALUATOR = etree.XPathEvaluator(etree.fromstring("<root></root>"))