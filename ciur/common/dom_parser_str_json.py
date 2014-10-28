#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ciur.common import DomParser
from advanced_types.advanced_ordered_dict import AdvancedOrderedDict


class DomParserStrJson(DomParser):
    """
    String implementation of DomParser
    1. Got xjson from Literal String
    3. return desired data form parsed page into json format
    name - name of parser just for debugging purposes
    source - file path to the json
    """

    def __init__(self, literal, name="default name", debug=False):
        self.abstract = False
        super(DomParserStrJson, self).__init__(name, literal, debug)
        self.context = AdvancedOrderedDict().load_json_from_str(literal)

        if not self.context:  # create new one
            self.context = {
                "name": self.name,
                "version": 0,
                "versions": []
            }

if __name__ == "__main__":
    s = """
    {
        "name": "",
        "test_url" : "JustinBieber_en.html",
        "version": 0,
        "versions": [{
            "version" : 0,
            "timestamp" : 0,
            "config" : {
                "xpath" : {
                    "root" : "//body",
                    "namespaces" : {}
                },
                "anomaly" : {
                    "root" : "//body",
                    "namespaces" : {}
                }
            },
            "anomaly" : {},
            "light_handlers" : {
                "^html:" : {},
                "^http_raise:bad_news" : {
                    "status_code": 404,
                    "message": "Justin Bieber Must Die"
                }
            },
            "bad_character_list": [],
            "rules" : {
                "h1": ["^http_raise:bad_news" , ".//h1[contains(text(), 'Justin Bieber did not spit on fans over balcony in Toronto, says rep')]"]
            },
            "blocks" : { },
            "reformat" : []
        }]
    }"""

    dpf = DomParserStrJson(s)
    xpath = dpf.get_version()
    dpf.validate_configs(xpath)
