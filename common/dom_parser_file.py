#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ciur.common import DomParser
from advanced_dict import AdvancedOrderedDict


class DomParserFile(DomParser):
    """
    File implementation of DomParser
    1. Got xjson from file
    2. Got page string
    3. return desired data form parsed page into json format
    name - name of parser just for debugging purposes
    source - file path to the json
    """
    def __init__(self, source, name="default name", debug=False):
        self.abstract = False
        super(DomParserFile, self).__init__(name, source, debug)
        self.context = AdvancedOrderedDict().load_json(self.source)

        if not self.context: # create new one
            self.context = {
                "name": self.name,
                "version": 0,
                "versions": [ ]
            }


    def __del__(self):
        s = super(DomParserFile, self)
        s.__del__()


    def save(self, js):
        super(DomParserFile, self).save(js)
        self.context.dump_json(self.source)
