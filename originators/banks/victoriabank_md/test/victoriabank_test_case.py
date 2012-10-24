#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest

from advanced_dict import AdvancedDict

from ciur.common.DomParserFile import DomParserFile


class VictoriabankTestCase(unittest.TestCase):
    def runTest(self):
        os.chdir(os.path.dirname(__file__))

        dpf = DomParserFile(
            name   = "test",
            source = "../xjsons/victoriabank.json"
        )
        for i in [1]:
            expect = AdvancedDict()
            expect.load_json("./expect/victoriabank_%02d.json" %i)
            expect = AdvancedDict.pretty_float(expect)

            xpath = dpf.get_version()
            dpf.validate_configs(xpath)
            with open("../page_samples/victoriabank_%02d.html" %i) as f: html = f.read()

            got = dpf.dive_html_root_level(html = html)
            print got.get_pretty()

            self.assertEqual(expect.comparable(), got.comparable())

