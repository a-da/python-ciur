#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from ciur.common import json_dump


class AdvancedDict(dict):
    """
    wrapper for dictionary datatype
    >>> a = AdvancedDict({"--" : "--"})
    >>> print a.get_pretty()
    {
        "--": "--"
    }

    >>> a = AdvancedDict('{"++" : {"b": "++"}}')
    >>> print a.get_pretty()
    {
        "++": {
            "b": "++"
        }
    }
    >>> print a.get_pretty("++.b")
    "++"

    >>> a = AdvancedDict(a)
    >>> print a.get_pretty()
    {
        "++": {
            "b": "++"
        }
    }

    >>> a = AdvancedDict()
    >>> print a.get_pretty()
    {}

    >>> a = AdvancedDict(None)
    >>> print a.get_pretty()
    {}

    >>> a = AdvancedDict({\
        "accounts": [\
            {\
                "email": "vector_soft_developer_test@yahoo.com",\
                "id": 0,\
                "pass": "Trust9",\
                "status": "Use a phone to verify your account"\
            },\
            {\
                "email": "vectorsoftX@hotmail.com",\
                "id": 1,\
                "pass": "N0ise-Full",\
                "status": "active"\
            }\
        ]\
    })
    >>> path = "/tmp/ciur_test_advanced_dict.json"
    >>> a.dump_json(path)
    >>> a.load_json(path)
    >>> print a.get_pretty()
    {
        "accounts": [
            {
                "email": "vector_soft_developer_test@yahoo.com",
                "id": 0,
                "pass": "Trust9",
                "status": "Use a phone to verify your account"
            },
            {
                "email": "vectorsoftX@hotmail.com",
                "id": 1,
                "pass": "N0ise-Full",
                "status": "active"
            }
        ]
    }
    """

    def __init__(self, *args, **kw):
        if args == (None, ) and kw == {}: # AdvancedDict(None)
            args = ()

        if len(args) and isinstance(args[0], (str, unicode)):
            args = (json.loads(args[0]),)

        super(AdvancedDict, self).__init__(*args, **kw)


    def __add__(self, x):
        """
        {} + {}
        """
        a = dict(self, **x)
        return AdvancedDict(a)


    def __sub__(self, x):
        """
        {} - {}
        """
        if isinstance(x, str):
            dict.__delitem__(self, x)

        return self


    def __getitem__(self, key):
        """
        {"a" : {"b" : "c"}}["a.b"] == c
        """
        # root path  .root.children
        if key.startswith("."):
            key = key[1:]

        keys = key.split(".")

        tmp = dict.__getitem__(self, keys[0])
        for i_key in keys[1:]:
            tmp = tmp.__getitem__(i_key)

        return tmp


    def has_key(self, key):
        """
        {"a" : {"b" : "c"}}.has_keys("a.b") == True
        """
        # root path  .root.children
        if key.startswith("."):
            key = key[1:]

        keys = key.split(".")

        if not dict.has_key(self, keys[0]):
            return False

        tmp = dict.__getitem__(self, keys[0])
        for i_key in keys[1:]:
            if not tmp.has_key(i_key):
                return False
            tmp = tmp.__getitem__(i_key)

        return True


    def get(self, key, default = None):
        """
        {"a" : {"b" : "c"}}.get("a.c", "0") == "0"
        """

        # root path  .root.children
        if key.startswith("."):
            key = key[1:]

        keys = key.split(".")

        if not self.has_key(keys[0]):
            return default

        tmp = dict.__getitem__(self, keys[0])

        for i_key in keys[1:]:
            if not (isinstance(tmp, dict) and tmp.has_key(i_key)):
                return default
            tmp = tmp.__getitem__(i_key)

        return tmp


    def get_utf8(self, key, default = None):
        """
        ensure to receive "utf-8" string not unicode
        {"a" : {"b" : "c"}}.get("a.c", "0") == "0"

        """
        tmp = self.get(key, default)

        tmp = tmp.encode("utf-8") if isinstance(tmp, unicode) else tmp
        return tmp


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
            dict.__setitem__(self, keys[0], value)
        else:
            tmp = dict.get(self, keys[0])
            if not tmp:
                tmp = {
                    keys[-1] : value
                }

                for i_key in keys[-2:0:-1]:
                    tmp = { i_key : tmp}

                dict.__setitem__(self, keys[0], tmp)
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
            dict.__delitem__(self, keys[0])
        else:
            tmp = dict.__getitem__(self, keys[0])
            for i_key in keys[1:-1]:
                tmp = tmp.__getitem__(i_key)

            tmp.__delitem__(keys[-1])


    def get_pretty(self, key_path = None):
        """
        json_dump(self).replace(", \n", ",\n").encode("utf-8")
        """

        # root path  .root.children
        if key_path and key_path.startswith("."):
            key_path = key_path[1:]

        dict_ = self[key_path] if key_path else self
        return json_dump(dict_).replace(", \n", ",\n").encode("utf-8")


    def rename_key(self, old_key, new_key, cast = None, mandatory=True):
        """
        self.rename("old", "new")
        self.rename("a.old", "new1")
        self.rename("old", "a.new2")
        """

        if mandatory or self.has_key(old_key):
            if cast:
                self[new_key] = cast(self[old_key])
            else:
                self.__setitem__(new_key, self.__getitem__(old_key))

            self.__delitem__(old_key)

        else: #don't raise error if key don't exist
            #print "skip rename"
            pass


    def rename_keys(self, arg_keys):
        """
        self.rename({ "from1" : ["into1", cast], "y.from2" : "g.into2"})
        or
        self.rename(( "from1" , "into1", cast, "y.from2" , "g.into2"))
        or
        self.rename([ "from1" , "into1", cast, "y.from2" , "g.into2"])
        """
        if isinstance(arg_keys, tuple) or isinstance(arg_keys, list):
            arg_keys_len = len(arg_keys)
            i = 0
            while i < arg_keys_len:
                if isinstance(arg_keys[i], type):
                    #print "!!", map_keys[i+1], map_keys[i+2], map_keys[i]
                    self.rename_key(arg_keys[i+1], arg_keys[i+2], arg_keys[i])
                    i += 3
                else:
                    #print "!", map_keys[i], map_keys[i+1]
                    self.rename_key(arg_keys[i], arg_keys[i+1])
                    i += 2
        elif isinstance(arg_keys, dict) or isinstance(arg_keys, AdvancedDict):
            for key, val in arg_keys.iteritems():
                if isinstance(val, str):
                    self.rename_key(key, val)
                else:
                    self.rename_key(key, val[0], cast=val[1])


    def load_json(self, file_path, clear = True):
        """
        loaf data from file *.json
        """
        if not os.path.isfile(file_path):
            dict_obj  = {}
        else:
            f = open(file_path, "r")
            db_config = f.read()
            f.close()

            dict_obj = json.loads(db_config)

        if clear:
            self.clear()

        self.__init__(dict_obj)


    def dump_json(self, file_path, sort_keys = False):
        """
        save data to file
        """
        str_js = json_dump(self, sort_keys = sort_keys).encode("utf-8")
        with open(file_path, "w") as f: f.write(str_js)



