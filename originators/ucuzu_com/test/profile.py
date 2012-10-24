def test_ucuzu_com_profile():
    """
    >>> test_ucuzu_com_profile()
    constructor DOMParser
    {
        "img": {
            "src": "ucuzu_com_profile_files/218937.jpg"
        },
        "sellers": [
            {
                "h_silver": 46958,
                "name": {
                    "href": "http://www.ucuzu.com/Jump.php?ProductAttributeId=308484545&ProductType=m&Price=0.03175&pp=1b3d30184014571cd6157fcd600e8391",
                    "onclick": "null,'UA-167882-5', '/outgoing/46958/Product', '3.09909625', 'product', 'Three Early Modern Utopias: Thomas More: Utopia / Francis Bacon: New Atlantis / Henry Neville: The Isle of Pines (Oxford World's Classics) (ISBN: 9780199537990)', '218937', '3283', 'Çađlayan Kitabevi');",
                    "text": "Çađlayan Kitabevi"
                },
                "price": "25,64 TL",
                "prod_name": "Three Early Modern Utopias: Thomas More: Utopia\\n / Francis Bacon: New Atlantis / Henry Neville: The Isle of Pines \\n(Oxford World's Classics)"
            }
        ],
        "summary": {
            "h_cat": 3283,
            "price": "25,64 TL'den",
            "title": "Three Early Modern Utopias: Thomas More: Utopia / Francis Bacon:\\n New Atlantis / Henry Neville: The Isle of Pines (Oxford World's \\nClassics) (ISBN: 9780199537990)"
        }
    }
    destructor DOMParser
    """
    dpf = DomParserFile(
        name = "test",
        source = "/oknetwiki/trunk/py_lib/vsft/test/ucuzu_com_profile.json"
    )

    xpath = dpf.get_version()

    dpf.validate_configs(xpath)

    html = open("/oknetwiki/trunk/py_lib/vsft/test/ucuzu_com_profile.html").read()

    m = dpf.dive_html_root_level(html = html, disable_br=False)

    print m.get_pretty()