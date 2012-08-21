#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from ciur.common.DomParserFile import DomParserFile
from ciur.util.AdvancedDict    import AdvancedDict

class AdvertTestCase(unittest.TestCase):
    def runTest(self):
        dpf = DomParserFile(
            name = "test",
            source = "../xjsons/advert.json"
        )

        expect = AdvancedDict()
        expect.load_json("./advert_01.json")

        xpath = dpf.get_version()
        dpf.validate_configs(xpath)
        with open("../page_samples/advert_01.html") as f: html = f.read()
        html = html.decode("utf-8")

        got = dpf.dive_html_root_level(html = html, disable_br = True)

        print got.get_pretty()
        self.assertEqual(expect, got)
