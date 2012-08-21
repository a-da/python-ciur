#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ciur.common.DomParserFile import DomParserFile
from ciur.util.AdvancedDict    import AdvancedDict
from node_test_case import NodeTestCase

class SearchCase(NodeTestCase):
    def runTest(self):
        dpf = DomParserFile(
            name = "test",
            source = "../xjsons/search.json"
        )
        xpath = dpf.get_version()
        dpf.validate_configs(xpath)

        expect = AdvancedDict()

        for i in range(3, 4):
            expect.load_json("./search_0%d.json" %i)
            with open("../page_samples/search_0%d.html" %i) as f: html = f.read()
            html = self._facebook_page_replace(html)
            got = dpf.dive_html_root_level(html = html, disable_br = False)
            self.assertEqual(expect, got, "diff in search_0%d" %i)

