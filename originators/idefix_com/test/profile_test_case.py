#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from ciur.common.DomParserFile import DomParserFile
from ciur.util.AdvancedDict    import AdvancedDict

class ProfileTestCase(unittest.TestCase):
    def runTest(self):
        expect = AdvancedDict()
        expect.load_json("./profile.json")
        dpf = DomParserFile(
            name = "test",
            source = "../xjsons/profile.json"
        )
        xpath = dpf.get_version()
        dpf.validate_configs(xpath)
        with open("../page_samples/profile_01.html") as f: html = f.read()
        got = dpf.dive_html_root_level(html = html, disable_br=False)

        self.assertEqual(expect, got)
