#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ciur.util.AdvancedDict import AdvancedDict

class AdvancedDictDomParser(AdvancedDict):
    """
    AdvancedDict implimentation for DomParser
    >>> a2 = AdvancedDictDomParser({\
        "1" : "1",\
        "2" : {\
            "3" : {\
            "4" : "patru"\
            },\
        "33" : {"44" : "4patru"}\
        }\
    })
    >>> a2.get_utf8("2.3", 555.999)
    {'4': 'patru'}
    >>> a2.rename_keys({"2.3": "2.13", "2.33" : "2.133"})
    >>> print a2.get_pretty()
    {
        "1": "1",
        "2": {
            "133": {
                "44": "4patru"
            },
            "13": {
                "4": "patru"
            }
        }
    }

    >>> d = AdvancedDictDomParser({"a" : "b"})
    >>> print d["a"]
    b
    >>> d["as"] = "cur"
    >>> d.dom_push("unu", "one")
    >>> print d.get_pretty()
    {
        "a": "b",
        "as": "cur",
        "unu": "one"
    }
    >>> d.dom_push("unu", ["a", "b"])
    >>> d.dom_push("unu", ["doi1", "doi2"])
    >>> d.dom_push("unu", ["trei1", "trei2"])
    >>> d.dom_push("unu", ["patru1", "patru2"])
    >>> print d.get_pretty()
    {
        "a": "b",
        "as": "cur",
        "unu": [
            "one",
            [
                "a",
                "b"
            ],
            [
                "doi1",
                "doi2"
            ],
            [
                "trei1",
                "trei2"
            ],
            [
                "patru1",
                "patru2"
            ]
        ]
    }

    >>> a = AdvancedDictDomParser({"--" : "--"})
    >>> print a.get_pretty()
    {
        "--": "--"
    }

    >>> a = AdvancedDictDomParser(a)
    >>> print a.get_pretty()
    {
        "--": "--"
    }

    >>> a = AdvancedDictDomParser()
    >>> print a.get_pretty()
    {}

    >>> a = AdvancedDictDomParser(None)
    >>> print a.get_pretty()
    {}
    """


    def __init__(self, *args, **kw):
        self.counter = {}
        super(AdvancedDictDomParser, self).__init__(*args, **kw)


    def dom_push(self, key, value, unique = False):
        """
        extension for DomParser class
        """
        if not (isinstance(value, (bool, float, long, int)) or value): #! do not change (ignore bool)
            return

        if not self.counter.has_key(key):
            self.counter[key] = 0

        if not self.has_key(key):
            self[key] = value
        else:
            if unique:
                if not self.counter[key] == 1:
                    self[key] = list({self[key], value})
                else:
                    self[key].append(value)
                    self[key] = list(set(self[key]))
            else:
                if self.counter[key] == 1:
                    self[key] = [self[key], value]
                else:
                    self[key].append(value)

        self.counter[key] += 1
