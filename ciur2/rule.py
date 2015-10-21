import ciur2
import json


class Rule(ciur2.CommonEqualityMixin):
    """
    >>> rule1 = Rule("root", "/h3", "dict",
    ...  Rule("name", ".//h1[contains(text(), 'Justin')]", "str"),
    ...  Rule("count_list", ".//h2[contains(text(), 'Andrei')]/p", ["list", "int"]),
    ...  Rule("user", ".//h5[contains(text(), 'Andrei')]/p", ["node"],
    ...         Rule("name", "./spam", "str"),
    ...         Rule("sure_name", "./bold", "str"),
    ...         Rule("age", "./it", "int"),
    ...         Rule("hobby", "./li", ["list", "str"]),
    ...         Rule("indexes", "./li/bold", ["list", "int"])
    ...       )
    ... )
    >>> res1 = json.dumps(rule1.to_dict(), indent=4)
    >>> print res1  # doctest: +NORMALIZE_WHITESPACE
    {
        "xpath": "/h3",
        "type_list": "dict",
        "name": "root",
        "rule": [
            {
                "xpath": ".//h1[contains(text(), 'Justin')]",
                "type_list": "str",
                "name": "name"
            },
            {
                "xpath": ".//h2[contains(text(), 'Andrei')]/p",
                "type_list": [
                    "list",
                    "int"
                ],
                "name": "count_list"
            },
            {
                "xpath": ".//h5[contains(text(), 'Andrei')]/p",
                "type_list": "node",
                "name": "user",
                "rule": [
                    {
                        "xpath": "./spam",
                        "type_list": "str",
                        "name": "name"
                    },
                    {
                        "xpath": "./bold",
                        "type_list": "str",
                        "name": "sure_name"
                    },
                    {
                        "xpath": "./it",
                        "type_list": "int",
                        "name": "age"
                    },
                    {
                        "xpath": "./li",
                        "type_list": [
                            "list",
                            "str"
                        ],
                        "name": "hobby"
                    },
                    {
                        "xpath": "./li/bold",
                        "type_list": [
                            "list",
                            "int"
                        ],
                        "name": "indexes"
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

        self.type_list = self._2complex(type_list)

    @classmethod
    def _2complex(cls, value):
        if not isinstance(value, list):
            return value,

        return value

    @classmethod
    def _2simple(cls, value):
        if isinstance(value, list):
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

        ret = {
            "name": self.name,
            "xpath": self.xpath,
            "type_list": self.type_list
        }

        rule = [i.to_dict() for i in self.rule]
        if rule:
            ret["rule"] = rule

        return ret

    def __repr__(self):
        return "ciur3.Rule(%s)" % self.to_dict()