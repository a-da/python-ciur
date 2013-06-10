def test_yellowpages_com_tr_profile():
    """
    >>> test_yellowpages_com_tr_profile()
    constructor DOMParser
    {
        "address": "Alaybey Mah. Mermerburnu Mevki No:31\\n<h2>Bozcaada Merkez, Bozcaada, Canakkale </h2>",
        "name": "Akvaryum Hotel",
        "phone": "+90 286 697 01 49",
        "seo_text": "<strong>\\n                                                Categorie(s):</strong> <a href=\\"http://www.yellowpages.com.tr/category/MTAyOTA=/Youth-Hostels.html\\" class=\\"category_link\\">Youth Hostels</a>",
        "web_site": "www.akvaryumbozcaada.com"
    }
    destructor DOMParser
    """
    dpf = DomParserFile(
        name = "test",
        source = "/oknetwiki/trunk/py_lib/vsft/test/yellowpages_com_tr_profile.json"
    )

    xpath = dpf.get_version()

    dpf.validate_configs(xpath)

    html = open("/oknetwiki/trunk/py_lib/vsft/test/yellowpages_com_tr_profile.html").read()

    m = dpf.dive_html_root_level(html = html)

    print m.get_pretty()