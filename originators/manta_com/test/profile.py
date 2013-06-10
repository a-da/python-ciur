def test_manta_com_profile():
    """
    >>> test_manta_com_profile()
    constructor DOMParser
    {
        "about": {
            "detailed": "Tiaxim-Grup Srl is a private company \\ncategorized under General Merchanise Stores and located in Chisinau, \\nMoldova.\\t\\tOur records show it was established in  and incorporated in  ."
        },
        "add_info": [
            "Miscellaneous general merchandise in Chisinau",
            "Miscellaneous General Merchandise Stores,",
            "All Other General Merchandise Stores"
        ],
        "company_info": {
            "address": {
                "country": "Moldova",
                "locality": "Chisinau",
                "postal_code": "MD-2055",
                "street": "16 Plopilor Str"
            },
            "org": {
                "href": "http://www.manta.com/ic/mw61rpf/md/tiaxim-grup-srl",
                "name": "Tiaxim-Grup Srl"
            },
            "phone": "22580358"
        },
        "contacts": [
            {
                "employees": {
                    "job_title": "Director",
                    "name": "Alexandru Vasile Tiucov",
                    "url": "http://www.manta.com/ics/mw61rpf/md/tiaxim-grup-srl?q=Alexandru%20Vasile%20Tiucov%20Tiaxim-Grup%20Srl&cx=000513454314247386359%3Aarvxicegnim&cof=FORID%3A10"
                },
                "img": "manta_com_profile_files/icon_contact.gif"
            }
        ],
        "parent_urls": [
            {
                "href": "http://www.manta.com/world/",
                "name": "World"
            },
            {
                "href": "http://www.manta.com/world/Europe/",
                "name": "Europe"
            },
            {
                "href": "http://www.manta.com/world/Europe/Moldova/",
                "name": "Moldova"
            },
            {
                "href": "http://www.manta.com/world/Europe/Moldova/-/Chisinau/",
                "name": "Chisinau"
            }
        ],
        "table_data": {
            "location_type": "Single Location",
            "naics_code": "452990,"
        }
    }
    destructor DOMParser
    """
    dpf = DomParserFile(
        name = "test",
        source = "/oknetwiki/trunk/py_lib/vsft/test/manta_com_profile.json"
    )

    xpath = dpf.get_version()

    dpf.validate_configs(xpath)

    html = open("/oknetwiki/trunk/py_lib/vsft/test/manta_com_profile.html").read()

    m = dpf.dive_html_root_level(html = html)

    print m.get_pretty()

