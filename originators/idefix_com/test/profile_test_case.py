#!/usr/bin/env python

import unittest

from ciur.common import DomParserFile
from advanced_types.advanced_dict import AdvancedDict


class ProfileTestCase(unittest.TestCase):
    def run_test(self):
        expect = AdvancedDict()
        expect.load_json("./profile.json")
        dpf = DomParserFile(
            name="test",
            source="../xjsons/profile.json"
        )
        xpath = dpf.get_version()
        dpf.validate_configs(xpath)

        html = open("../page_samples/profile_01.html").read()

        got = dpf.dive_html_root_level(html=html, disable_br=False)

        self.assertEqual(expect, got)
