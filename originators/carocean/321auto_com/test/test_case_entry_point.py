#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from ciur.common   import DomParserFile
from advanced_dict import AdvancedDict

class EntryPointTestCase(unittest.TestCase):
    def runTest(self):
        dpf = DomParserFile(
            name = "test",
            source = "../xjsons/entry_point.json"
        )

        expect = AdvancedDict()
        expect.load_json("./expect/entry_point_01.json")

        xpath = dpf.get_version()
        dpf.validate_configs(xpath)
        with open("../page_samples/entry_point_01.html") as f: html = f.read()
        html = html.decode("iso-8859-1")
        got = dpf.dive_html_root_level(html = html, disable_br=False)

        print got.get_pretty()
        self.assertEqual(expect, got)
