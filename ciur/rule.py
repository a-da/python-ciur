"""
ciur internal dsl (python api)
"""
from collections import OrderedDict
from types import FunctionType
import json

import ciur
import ciur.cast
from ciur import pretty_json
import re

_JSON = basestring

_SELECTOR_TYPE_SET = {"xpath", "css"}


class Rule(ciur.CommonEqualityMixin):
    """
    >>> rule1 = Rule("root", "/h3", "+",
    ...  Rule("name", ".//h1[contains(., 'Justin')]/text()", "+1"),
    ...  Rule("count_list", ".//h2[contains(., 'Andrei')]/p", ["int", "+"]),
    ...  Rule("user", ".//h5[contains(., 'Andrei')]/p", "+",
    ...         Rule("name", "./spam/text()", "+1"),
    ...         Rule("sure_name", "./bold/text()", "+1"),
    ...         Rule("age", "./it", "int"),
    ...         Rule("hobby", "./li/text()", "+"),
    ...         Rule("indexes", "./li/bold", ["int", "+"])
    ...       )
    ... )
    >>> res1 = pretty_json(rule1.to_dict())
    >>> print res1  # doctest: +NORMALIZE_WHITESPACE
    {
        "name": "root",
        "selector": "/h3",
        "selector_type": "xpath",
        "type_list": "+",
        "rule": [
            {
                "name": "name",
                "selector": ".//h1[contains(., 'Justin')]/text()",
                "selector_type": "xpath",
                "type_list": "+1"
            },
            {
                "name": "count_list",
                "selector": ".//h2[contains(., 'Andrei')]/p",
                "selector_type": "xpath",
                "type_list": [
                    "int",
                    "+"
                ]
            },
            {
                "name": "user",
                "selector": ".//h5[contains(., 'Andrei')]/p",
                "selector_type": "xpath",
                "type_list": "+",
                "rule": [
                    {
                        "name": "name",
                        "selector": "./spam/text()",
                        "selector_type": "xpath",
                        "type_list": "+1"
                    },
                    {
                        "name": "sure_name",
                        "selector": "./bold/text()",
                        "selector_type": "xpath",
                        "type_list": "+1"
                    },
                    {
                        "name": "age",
                        "selector": "./it",
                        "selector_type": "xpath",
                        "type_list": "int"
                    },
                    {
                        "name": "hobby",
                        "selector": "./li/text()",
                        "selector_type": "xpath",
                        "type_list": "+"
                    },
                    {
                        "name": "indexes",
                        "selector": "./li/bold",
                        "selector_type": "xpath",
                        "type_list": [
                            "int",
                            "+"
                        ]
                    }
                ]
            }
        ]
    }

    >>> rule2 = Rule.from_dict(res1)
    >>> rule1.to_dict() == rule2.to_dict()
    True
    >>> rule1 == rule2
    True
    """

    def __init__(self, name, selector, type_list_, *selector_type_and_or_rule):
        self.name = name
        self.selector = selector

        if not selector_type_and_or_rule:
            self.selector_type = "xpath"
            self.rule = ()
        else:
            if selector_type_and_or_rule[0] in _SELECTOR_TYPE_SET:
                self.selector_type = selector_type_and_or_rule[0]
                self.rule = selector_type_and_or_rule[1]
            else:
                self.selector_type = "xpath"
                self.rule = selector_type_and_or_rule

        # mutable object is eval !
        if isinstance(self.rule, list):
            self.rule = tuple(self.rule)

        tmp = []

        for type_i in self._2complex(type_list_):
            #  assert isinstance(type_i, basestring)

            if isinstance(type_i, list):
                func_name = type_i[0]
                args = type_i[1:]

            else:
                m = re.search("^([\*\+])(\d+)?$", type_i)
                if m:
                    func_name = "size"
                    args = (
                        "mandatory" if m.group(1) == "+" else "optional",
                        int(m.group(2) or 0),
                    )
                else:
                    func_name = type_i
                    args = tuple()

            tmp.append([getattr(ciur.cast, func_name + "_"), args])

        self.type_list = tmp

    @classmethod
    def _2complex(cls, value):
        if not isinstance(value, list):
            return (value, )

        return value

    @classmethod
    def _2simple(cls, value):
        if isinstance(value, (list, tuple)):
            tmp = []
            for value_i in value:
                tmp_i = value_i
                if isinstance(value_i[0], FunctionType):
                    function = value_i[0].__name__
                    if function == "size_":
                        tmp_i = "%s%s" % (
                            "+" if value_i[1][0] == "mandatory" else "*",
                            "" if value_i[1][1] == 0 else value_i[1][1]
                        )
                    else:
                        if not value_i[1]:
                            tmp_i = ("%s" % function[:-1]).encode("utf-8")

                tmp.append(tmp_i)
            value = tmp

            if len(value) == 1:
                return value[0]

        return value

    @staticmethod
    def from_dict(dict_):
        # TODO: check load root list

        assert isinstance(dict_, (dict, _JSON))

        if isinstance(dict_, _JSON):
            dict_ = json.loads(dict_)

        # check for children [] means no children
        rule = [Rule.from_dict(rule) for rule in dict_.get("rule", [])]

        return Rule(
            dict_["name"], dict_["selector"], dict_["type_list"],
            *(dict_.get("selector_type", "xpath"), rule)
        )

    @staticmethod
    def from_list(list_):
        return ListOfT(Rule.from_dict(i) for i in list_)

    def to_dict(self):

        ret = OrderedDict()
        ret["name"] = self.name
        ret["selector"] = self.selector
        ret["selector_type"] = self.selector_type
        ret["type_list"] = self._2simple(self.type_list)

        rule = [i.to_dict() for i in self.rule]
        if rule:
            ret["rule"] = rule

        return ret

    def __repr__(self):
        return "%s.%s(%s)" % (self.__class__.__module__, self.__class__.__name__, self.to_dict())

    def __str__(self):
        pretty = pretty_json(self.to_dict())
        return "%s.%s(%s)" % (self.__class__.__module__, self.__class__.__name__, pretty)


class ListOfT(list):
    """
    wrapper for List Of Dict
    The purpose is to have pretty print option for that complex type
    """
    @classmethod
    def _callback(cls, x):
        return x

    def __str__(self):
        name = "%s.%s:" % (self.__class__.__module__, self.__class__.__name__)
        res = name + "".join(
            "\n-----------%d-\n%s" % (index, self._callback(t)) for index, t in enumerate(self, 1)
        ).replace("\n", "\n    ")

        return res


class ListOfDict(ListOfT):
    """
    wrapper for List Of Dict
    The purpose is to have pretty print option for that complex type
    """
    @classmethod
    def _callback(cls, x):
        return pretty_json(x)
