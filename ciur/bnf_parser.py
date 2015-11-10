"""
ciur external dsl

>>> import pprint
>>> bnf = get_bnf()

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
import json

from pyparsing import (
    col,
    lineEnd,
    empty,
    alphas,
    alphanums,
    printables,
    pythonStyleComment
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

_indent_stack = [1]


def _check_peer_indent(s, l, t):
    cur_col = col(l, s)
    if cur_col != _indent_stack[-1]:
        if (not _indent_stack) or cur_col > _indent_stack[-1]:
            raise ParseFatalException(s, l, "illegal nesting")
        raise ParseException(s, l, "not a peer entry ????")


def _check_sub_indent(s, l, t):
    cur_col = col(l, s)
    if cur_col > _indent_stack[-1]:
        _indent_stack.append(cur_col)
    else:
        raise ParseException(s, l, "not a subentry")


def _check_unindent(s, l):
    if l >= len(s):
        return

    cur_col = col(l, s)
    if not(cur_col < _indent_stack[-1] and cur_col <= _indent_stack[-2]):
        raise ParseException(s, l, "not an unindent")


def do_unindent():
    _indent_stack.pop()


def get_bnf():
    grave = Suppress("`")
    indent = lineEnd.suppress() + empty + empty.copy().setParseAction(_check_sub_indent)
    undent = FollowedBy(empty).setParseAction(_check_unindent).setParseAction(do_unindent)

    identifier = Word(alphas, alphanums + "_")  # <url> ./url str +1 => label of rule

    # url <./url> str +1 => xpath query
    xpath = grave + Word(alphas+"./", printables + " ", excludeChars="`") + grave

    type_list = Group(
        Optional(Literal("str") | Literal("int")) +  # url ./url <str> +1 => functions chains for transformation
        Regex("[\+*]\d*")   # url ./url str <+1>  => size match: + mandatory, * optional, \d+ exact len
    )

    rule = (identifier + xpath + type_list)  # <url ./url str +1> => rule line

    stmt = Forward().setParseAction(_check_peer_indent)
    bnf = OneOrMore(stmt)

    children = Group(indent + bnf + undent).ignore(pythonStyleComment)
    stmt << Group(rule + Optional(children))  # check for children

    return bnf


def get_list(rules):
    bnf = get_bnf()
    parse_tree = bnf.parseString(rules, parseAll=True)
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

    return json.dumps(data, indent=4)


def to_dict(rules):
    list_ = get_list(rules)

    data = _to_dict(list_)

    return data
