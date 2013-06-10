#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import unittest

from ciur.common.DomParserFile import DomParserFile
from ciur.util.AdvancedDict    import AdvancedDict

class NodeTestCase(unittest.TestCase):
    @staticmethod
    def _facebook_page_replace(html):
        html = re.sub('( class="(?:.*? )?)hidden_elem((?: .*?)?")', lambda m: m.group(1) + "__hidden_elem__" + m.group(2), html)
        html = html.replace("<!--", "").replace("-->", "")
        return html

    def runTest(self):
        dpf = DomParserFile(
            name = "test",
            source = "../xjsons/node.json"
        )
        xpath = dpf.get_version()
        dpf.validate_configs(xpath)

        expect = AdvancedDict()

        expect.load_json("./expect/node.json")
        with open("../page_samples/node.html") as f: html = f.read()
        html = self._facebook_page_replace(html)
        got = dpf.dive_html_root_level(html = html, disable_br=False)
        self.assertEqual(expect, got)
