#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import decimal

from collections            import OrderedDict
from ciur.common            import json_dump
from ciur.util.AdvancedDict import AdvancedDict


class AdvancedOrderedDict(OrderedDict, AdvancedDict):
    """
    wrapper for dictionary data type
    >>> a = AdvancedOrderedDict({"--" : "--"})
    >>> print a.get_pretty()
    {
        "--": "--"
    }

    >>> a = AdvancedOrderedDict('{"++" : {"b": "++"}}')
    >>> print a.get_pretty()
    {
        "++": {
            "b": "++"
        }
    }
    >>> print a.get_pretty("++.b")
    "++"

    >>> a = AdvancedOrderedDict(a)
    >>> print a.get_pretty()
    {
        "++": {
            "b": "++"
        }
    }

    >>> a = AdvancedOrderedDict()
    >>> print a.get_pretty()
    {}

    >>> a = AdvancedOrderedDict(None)
    >>> print a.get_pretty()
    {}

    >>> a = AdvancedOrderedDict({"b" : "a"})
    >>> a.update({\
        "accounts": [\
            {\
                "status": "Use a phone to verify your account",\
                "pass": "Trust9",\
                "email": "vector_soft_developer_test@yahoo.com",\
                "id": 0\
            },\
            {\
                "status": "active",\
                "pass": "N0ise-Full",\
                "email": "vectorsoftX@hotmail.com",\
                "id": 1\
            }\
        ]\
    })
    >>> path = "/tmp/ciur_test_advanced_ordered_dict.json"
    >>> a.dump_json(path)
    >>> a.load_json(path)
    >>> print a.get_pretty()
    {
        "b": "a",
        "accounts": [
            {
                "status": "Use a phone to verify your account",
                "id": 0,
                "email": "vector_soft_developer_test@yahoo.com",
                "pass": "Trust9"
            },
            {
                "status": "active",
                "id": 1,
                "email": "vectorsoftX@hotmail.com",
                "pass": "N0ise-Full"
            }
        ]
    }
    """

    def __init__(self, *args, **kw):
        if args == (None, ) and kw == {}: # AdvancedDict(None)
            args = ()

        if len(args) and isinstance(args[0], (str, unicode)):
            args = (json.loads(args[0]),)

        super(AdvancedOrderedDict, self).__init__(*args, **kw)


    def __setitem__(self, key, value):
        """
        {"a" : {"b" : "c"}}["a.c"] = 10
        {"a" : {"b" : "c", "c" : 10}}
        """
        # root path  .root.children
        if key.startswith("."):
            key = key[1:]

        keys = key.split(".")

        if keys.__len__() == 1:
            OrderedDict.__setitem__(self, keys[0], value)
        else:
            tmp = OrderedDict.get(self, keys[0])
            if not tmp:
                tmp = {
                    keys[-1] : value
                }

                for i_key in keys[-2:0:-1]:
                    tmp = { i_key : tmp}

                OrderedDict.__setitem__(self, keys[0], tmp)
            else:
                for i_key in keys[1:-1]:
                    tmp = tmp.__getitem__(i_key)

                tmp.__setitem__(keys[-1], value)

    def __delitem__(self, key):
        """
        del {"a" : {"b" : "c", "c" : 10}}["a.c"]
        {"a" : {"b" : "c"}
        """
        # root path  .root.children
        if key.startswith("."):
            key = key[1:]

        keys = key.split(".")

        if keys.__len__() == 1:
            OrderedDict.__delitem__(self, keys[0])
        else:
            tmp = OrderedDict.__getitem__(self, keys[0])
            for i_key in keys[1:-1]:
                tmp = tmp.__getitem__(i_key)

            tmp.__delitem__(keys[-1])


    def get_pretty(self, key_path = None):
        """
        json_dump(self).replace(", \n", ",\n").encode("utf-8")
        """
        dict_ = self[key_path] if key_path else self
        return json_dump(dict_, sort_keys=False).replace(", \n", ",\n").encode("utf-8")


    def load_json(self, file_path, clear = True):
        """
        loaf data from file
        """
        if not os.path.isfile(file_path):
            dict_obj  = {}
        else:
            f = open(file_path, "r")
            db_config = f.read()
            f.close()

            dict_obj = json.loads(
                db_config,
                object_pairs_hook = OrderedDict,
                parse_float       = decimal.Decimal
            )

        if clear:
            self.clear()

        self.__init__(dict_obj)