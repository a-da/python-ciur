#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ciur.common    import DomParserFile
from advanced_dict  import AdvancedDict
from node_test_case import NodeTestCase

class ProfileCase(NodeTestCase):
    def runTest(self):
        dpf = DomParserFile(
            name = "test",
            source = "../xjsons/profile.json"
        )
        xpath = dpf.get_version()
        dpf.validate_configs(xpath)

        expect = AdvancedDict()

        for i in range(1, 11):
            expect.load_json("./expect/profile_%02d.json" %i)

            with open("../page_samples/profile_%02d.html" %i) as f: html = f.read()
            html = self._facebook_page_replace(html)
            got = dpf.dive_html_root_level(html = html)
            self.assertEqual(expect, got, "diff in profile_%02d" %i)
