Testing http://scrapy.org/companies/
====================================

>>> from ciur import parse, pretty_json
>>> from ciur.rule import Rule
>>> import requests

>>> requests = requests.Session()
>>> response = requests.get("http://scrapy.org/companies/")

test internal dsl
-----------------

>>> rule = Rule("company_list", ".//div[@class='company-box']", "+",
...             Rule("name", ".//span[@class='highlight']/text()", ["+"]),
...             Rule("company_url", "./a/@href", ["+1"]),
...             Rule("blog_url", "./p/a/@href", ["*"]),
...             Rule("logo", "./a/img/@src", ["+"])
...            )

>>> data = parse.html(response.content, rule)
>>> print pretty_json(data)  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    {
            "company_list": [
                {
                    "name": "Scrapinghub:",
                    "company_url": "http://scrapinghub.com/",
                    "blog_url": "http://scrapinghub.com/about",
                    "logo": "../img/shub-logo.png"
                },
                ...
                {
                    "name": "El Útero de Marita:",
                    "company_url": "http://utero.pe/",
                    "logo": "../img/40-utero-logo.png"
                },
                ...
                {
                    "name": "SayOne:",
                    "company_url": "http://sayonetech.com/",
                    "logo": "../img/sayone-logo.png"
                }
            ]
    }

test external dsl
-----------------

>>> from ciur import bnf_parser
>>> res = bnf_parser.to_dict(open("ciur.d/scrapy.org_support.ciur"))
>>> rule = Rule.from_dict(res[0])  # doctest: +NORMALIZE_WHITESPACE
>>> data = parse.html(response.content, rule)
>>> print pretty_json(data)  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    {
        "company_list": [
        {
            "name": "Scrapinghub:",
            "company_url": "http://scrapinghub.com/",
            "blog_url": "http://scrapinghub.com/about",
            "logo": "../img/shub-logo.png"
        },
        ...
        {
            "name": "SayOne:",
            "company_url": "http://sayonetech.com/",
            "logo": "../img/sayone-logo.png"
        }
        ]
    }