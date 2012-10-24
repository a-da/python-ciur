#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest

from advanced_dict import AdvancedDict

from ciur.common.DomParserFile import DomParserFile


class BCRTestCase(unittest.TestCase):
    def runTest(self):
        os.chdir(os.path.dirname(__file__))

        dpf = DomParserFile(
            name = "test",
            source = "../xjsons/bcr.json"
        )

        expect = AdvancedDict()
        expect.load_json("./expect/bcr_01.json")
        expect = expect.pretty_float(expect)


        xpath = dpf.get_version()
        dpf.validate_configs(xpath)
        with open("../page_samples/bcr_01.html") as f: html = f.read()

        got = dpf.dive_html_root_level(html = html)
        print got.get_pretty()

        self.assertEqual(expect.comparable(), got.comparable())

