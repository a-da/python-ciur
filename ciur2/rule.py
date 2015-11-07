from collections import OrderedDict
from types import FunctionType
import ciur2
import json


class Rule(ciur2.CommonEqualityMixin):
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

    def __init__(self, name, xpath, type_list, *rule):
        self.name = name
        self.xpath = xpath
        self.rule = rule

        import ciur2.cast
        tmp = []

        for type_i in self._2complex(type_list):
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

            tmp.append([getattr(ciur2.cast, func_name + "_"), args])

        self.type_list = tuple(tmp)


    @classmethod
    def _2complex(cls, value):
        if not isinstance(value, list):
            return value,

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
        if isinstance(dict_, str):
            dict_ = json.loads(dict_)

        rule = [Rule.from_dict(rule) for rule in dict_.get("rule", [])]

        return Rule(dict_["name"], dict_["xpath"], dict_["type_list"], *rule)

    def to_dict(self):
        self.type_list = self._2simple(self.type_list)

        ret = OrderedDict()
        ret["name"] = self.name
        ret["xpath"] = self.xpath
        ret["type_list"] = self.type_list

        rule = [i.to_dict() for i in self.rule]
        if rule:
            ret["rule"] = rule

        return ret

    def __repr__(self):
        return "ciur3.Rule(%s)" % self.to_dict()