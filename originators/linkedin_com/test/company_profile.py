#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_linkedin_com_company_profile():
    """
    >>> test_linkedin_com_company_profile()
    constructor DOMParser
    {
        "basic_info": {
            "company_size": "501-1000 employees",
            "founded": 2000,
            "industry": "Information Technology and Services",
            "type": "Privately Held",
            "website": {
                "href": "http://www.linkedin.com/redirect?url=http%3A%2F%2Fwww%2Eendava%2Ecom&urlhash=u-sD",
                "name": "http://www.endava.com"
            }
        },
        "location": {
            "adr": {
                "country_name": "United Kingdom",
                "locality": "London,",
                "postal_code": "EC2N 1AR",
                "region": "UK",
                "street": [
                    "London Office",
                    "125 Old Broad Street"
                ]
            },
            "map": {
                "img": "linkedin_com_company_profile_files/staticmap.png",
                "link": "http://maps.google.com/maps?q=London%20Office+125%20Old%20Broad%20Street+London+EC2N%201AR+United%20Kingdom"
            }
        },
        "logo": [
            "linkedin_com_company_profile_files/1a01087.png"
        ],
        "name": "Endava",
        "text_desc": {
            "desc": "Endava is a well-established IT Services company, with over 700 full\\n time employees working across its European development centres, London \\nheadquarters and further offices in the US. Formed in 2000, Endava is \\nuniquely placed within the IT services sector as it employs an optimum \\nblend of onshore consultancy, project management and nearshore IT \\nservice delivery.",
            "specialties": "Application Development,\\n Application Managament,\\n Testing,\\n Digital Media,\\n Hosting,\\n Agile,\\n Planned Iterative,\\n Nearshore,\\n Infrastructure Management"
        }
    }
    destructor DOMParser
    """
    dpf = DomParserFile(
        name = "test",
        source = "/oknetwiki/trunk/py_lib/vsft/test/linkedin/linkedin_com_company_profile.json"
    )

    xpath = dpf.get_version()

    dpf.validate_configs(xpath)

    html = open("/oknetwiki/trunk/py_lib/vsft/test/linkedin/linkedin_com_company_profile.html").read()

    m = dpf.dive_html_root_level(html = html, disable_br=False)

    print m.get_pretty()
