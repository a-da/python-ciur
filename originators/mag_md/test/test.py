#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_mag_md():
    """
    >>> test_mag_md()
    constructor DOMParser
    {
        "ara": [
            {
                "doi": "_text doi are1",
                "unu": "_text unu ara1"
            }
        ],
        "float1": -99.847477777,
        "float6": -99.85,
        "int1": 100,
        "int2": 20,
        "int3": -20,
        "int4": 280648,
        "int5": -99,
        "title": "Интернет-магазин Mag.md"
    }
    destructor DOMParser
    """
    dpf = DomParserFile(name = "test", source = "/oknetwiki/trunk/py_lib/vsft/test/mag_md_profile.json")
    xpath = dpf.get_version()
    dpf.validate_configs(xpath)

    html = open("/oknetwiki/trunk/py_lib/vsft/test/mag_md_profile.html").read()

    def fun_lol(value):
        return value ** 2
    m = dpf.dive_html_root_level(html = html, handlers=[fun_lol])

    print m.get_pretty()
