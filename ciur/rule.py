"""
ciur internal dsl (python api)
"""
from collections import OrderedDict
from types import FunctionType
import json

import ciur
import ciur.cast
from ciur import pretty_json

JSON = basestring


class Rule(ciur.CommonEqualityMixin):
    """
    >>> rule1 = Rule("root", "/h3", "+",
    ...  Rule("name", ".//h1[contains(text(), 'Justin')]", "str"),
    ...  Rule("count_list", ".//h2[contains(text(), 'Andrei')]/p", ["int", "+"]),
    ...  Rule("user", ".//h5[contains(text(), 'Andrei')]/p", "+",
    ...         Rule("name", "./spam", "str"),
    ...         Rule("sure_name", "./bold", "str"),
    ...         Rule("age", "./it", "int"),
    ...         Rule("hobby", "./li", ["str", "+"]),
    ...         Rule("indexes", "./li/bold", ["int", "+"])
    ...       )
    ... )
    >>> res1 = json.dumps(rule1.to_dict(), indent=4)
    >>> print res1  # doctest: +NORMALIZE_WHITESPACE
    {
        "name": "root",
        "xpath": "/h3",
        "type_list": "+",
        "rule": [
            {
                "name": "name",
                "xpath": ".//h1[contains(text(), 'Justin')]",
                "type_list": "str"
            },
            {
                "name": "count_list",
                "xpath": ".//h2[contains(text(), 'Andrei')]/p",
                "type_list": [
                    "int",
                    "+"
                ]
            },
            {
                "name": "user",
                "xpath": ".//h5[contains(text(), 'Andrei')]/p",
                "type_list": "+",
                "rule": [
                    {
                        "name": "name",
                        "xpath": "./spam",
                        "type_list": "str"
                    },
                    {
                        "name": "sure_name",
                        "xpath": "./bold",
                        "type_list": "str"
                    },
                    {
                        "name": "age",
                        "xpath": "./it",
                        "type_list": "int"
                    },
                    {
                        "name": "hobby",
                        "xpath": "./li",
                        "type_list": [
                            "str",
                            "+"
                        ]
                    },
                    {
                        "name": "indexes",
                        "xpath": "./li/bold",
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

    def __init__(self, name, xpath, type_list_, *rule):
        self.name = name
        self.xpath = xpath
        self.rule = rule

        tmp = []

        for type_i in self._2complex(type_list_):
            assert isinstance(type_i, basestring)
            import re
            m = re.search("^([\*\+])(\d+)?$", type_i)
            if m:
                func_name = "size"
                args = (
                    "mandatory" if m.group(1) == "+" else "optional",
                    int(m.group(2) or 0),
                )
            else:
                if isinstance(type_i, list):
                    func_name = type_i[:1]
                    args = type_i[1:]
                else:
                    func_name = type_i
                    args = tuple()

            tmp.append([getattr(ciur.cast, func_name + "_"), args])

        self.type_list = tmp

        i = 100

    @classmethod
    def _2complex(cls, value):
        if not isinstance(value, list):
            return tuple(value)

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

        assert isinstance(dict_, (dict, JSON))

        if isinstance(dict_, JSON):
            dict_ = json.loads(dict_)

        # check for children [] means no children
        rule = [Rule.from_dict(rule) for rule in dict_.get("rule", [])]

        return Rule(dict_["name"], dict_["xpath"], dict_["type_list"], *rule)

    @staticmethod
    def from_list(list_):
        # for i in list_:
        #     yield Rule.from_dict(i)
        return ListOfT(Rule.from_dict(i) for i in list_)
        # return ListOfDict(list_)
        #return ListOfRule(list_)

    def to_dict(self):

        ret = OrderedDict()
        ret["name"] = self.name
        ret["xpath"] = self.xpath
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
