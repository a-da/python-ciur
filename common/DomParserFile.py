#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from ciur.common.DomParser import DomParser
from ciur.util.AdvancedOrderedDict import AdvancedOrderedDict

class DomParserFile(DomParser):
    """
    File implimentation of DomParser
    1. Got xjson from file
    2. Got page string
    3. return desired data form parsed page into json format
    """
    def __init__(self, name, source, debug = False):
        self.abstract = False
        super(DomParserFile, self).__init__(name, source, debug)
        self.context = AdvancedOrderedDict()
        self.context.load_json(self.source)

        if not self.context: # create new one
            self.context = {
                "name" : self.name,
                "version" : 0,
                "versions" : [ ]
            }


    def __del__(self):
        s = super(DomParserFile, self)
        s.__del__()


    def save(self, js):
        super(DomParserFile, self).save(js)
        self.context.dump_json(self.source)
