def test_manta_com_country():
    """
    >>> test_manta_com_country()
    constructor DOMParser
    {
        "paths": [
            {
                "name": "Albania",
                "path": "/world/Europe/Albania/"
            },
            {
                "name": "Andorra",
                "path": "/world/Europe/Andorra/"
            },
            {
                "name": "Armenia",
                "path": "/world/Europe/Armenia/"
            },
            {
                "name": "Austria",
                "path": "/world/Europe/Austria/"
            },
            {
                "name": "Azerbaijan",
                "path": "/world/Europe/Azerbaijan/"
            },
            {
                "name": "Belarus",
                "path": "/world/Europe/Belarus/"
            },
            {
                "name": "Belgium",
                "path": "/world/Europe/Belgium/"
            },
            {
                "name": "Bosnia-Herzegovina",
                "path": "/world/Europe/Bosnia-Herzegovina/"
            },
            {
                "name": "Bulgaria",
                "path": "/world/Europe/Bulgaria/"
            },
            {
                "name": "Croatia",
                "path": "/world/Europe/Croatia/"
            },
            {
                "name": "Cyprus",
                "path": "/world/Europe/Cyprus/"
            },
            {
                "name": "Czech Republic",
                "path": "/world/Europe/Czech+Republic/"
            },
            {
                "name": "Denmark",
                "path": "/world/Europe/Denmark/"
            },
            {
                "name": "Estonia",
                "path": "/world/Europe/Estonia/"
            },
            {
                "name": "Faroe Islands",
                "path": "/world/Europe/Faroe+Islands/"
            },
            {
                "name": "Finland",
                "path": "/world/Europe/Finland/"
            },
            {
                "name": "France",
                "path": "/world/Europe/France/"
            },
            {
                "name": "Georgia",
                "path": "/world/Europe/Georgia/"
            },
            {
                "name": "Germany",
                "path": "/world/Europe/Germany/"
            },
            {
                "name": "Gibraltar",
                "path": "/world/Europe/Gibraltar/"
            },
            {
                "name": "Greece",
                "path": "/world/Europe/Greece/"
            },
            {
                "name": "Hungary",
                "path": "/world/Europe/Hungary/"
            },
            {
                "name": "Iceland",
                "path": "/world/Europe/Iceland/"
            },
            {
                "name": "Ireland",
                "path": "/world/Europe/Ireland/"
            },
            {
                "name": "Italy",
                "path": "/world/Europe/Italy/"
            },
            {
                "name": "Latvia",
                "path": "/world/Europe/Latvia/"
            },
            {
                "name": "Liechtenstein",
                "path": "/world/Europe/Liechtenstein/"
            },
            {
                "name": "Lithuania",
                "path": "/world/Europe/Lithuania/"
            },
            {
                "name": "Luxembourg",
                "path": "/world/Europe/Luxembourg/"
            },
            {
                "name": "Macedonia",
                "path": "/world/Europe/Macedonia/"
            },
            {
                "name": "Malta",
                "path": "/world/Europe/Malta/"
            },
            {
                "name": "Moldova",
                "path": "/world/Europe/Moldova/"
            },
            {
                "name": "Monaco",
                "path": "/world/Europe/Monaco/"
            },
            {
                "name": "Netherlands",
                "path": "/world/Europe/Netherlands/"
            },
            {
                "name": "Norway",
                "path": "/world/Europe/Norway/"
            },
            {
                "name": "Poland",
                "path": "/world/Europe/Poland/"
            },
            {
                "name": "Portugal",
                "path": "/world/Europe/Portugal/"
            },
            {
                "name": "Romania",
                "path": "/world/Europe/Romania/"
            },
            {
                "name": "San Marino",
                "path": "/world/Europe/San+Marino/"
            },
            {
                "name": "Serbia & Montenegro",
                "path": "/world/Europe/Serbia+&+Montenegro/"
            },
            {
                "name": "Slovakia",
                "path": "/world/Europe/Slovakia/"
            },
            {
                "name": "Slovenia",
                "path": "/world/Europe/Slovenia/"
            },
            {
                "name": "Spain",
                "path": "/world/Europe/Spain/"
            },
            {
                "name": "Sweden",
                "path": "/world/Europe/Sweden/"
            },
            {
                "name": "Switzerland",
                "path": "/world/Europe/Switzerland/"
            },
            {
                "name": "Ukraine",
                "path": "/world/Europe/Ukraine/"
            },
            {
                "name": "United Kingdom",
                "path": "/world/Europe/United+Kingdom/"
            }
        ]
    }
    destructor DOMParser
    """
    dpf = DomParserFile(
        name = "test",
        source = "/oknetwiki/trunk/py_lib/vsft/test/manta_com_country.json"
    )

    xpath = dpf.get_version()

    dpf.validate_configs(xpath)

    html = open("/oknetwiki/trunk/py_lib/vsft/test/manta_com_country.html").read()

    m = dpf.dive_html_root_level(html = html)

    print m.get_pretty()
