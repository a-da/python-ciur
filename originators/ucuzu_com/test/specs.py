#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_ucuzu_com_specs():
    """
    >>> test_ucuzu_com_specs()
    constructor DOMParser
    {
        "desc": "<div id=\\"product-description\\"></div>",
        "sheet": "<table cellpadding=\\"0\\" cellspacing=\\"0\\" id=\\"product-sheet\\">\\n<tbody><tr><td colspan=\\"2\\" style=\\"border: 0pt none;\\" class=\\"g\\">Özellikler</td></tr>  <tr>\\n    <td class=\\"p\\">Medya etiketleri</td>\\n    <td class=\\"v\\">\\n              Felsefe, Yabancý Dil          </td>\\n  </tr>\\n</tbody></table>"
    }
    destructor DOMParser
    """
    dpf = DomParserFile(
        name = "test",
        source = "/oknetwiki/trunk/py_lib/vsft/test/ucuzu_com_specs.json"
    )

    xpath = dpf.get_version()

    dpf.validate_configs(xpath)

    html = open("/oknetwiki/trunk/py_lib/vsft/test/ucuzu_com_specs.html").read()

    m = dpf.dive_html_root_level(html = html, disable_br=False)

    print m.get_pretty()