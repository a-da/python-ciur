Testing http://import.io/~ourjobs
=================================

>>> from ciur import parse, pretty_json
>>> from ciur.rule import Rule
>>> import requests

>>> requests = requests.Session()
>>> response = requests.get("http://import.io/~ourjobs")

test internal dsl
-----------------

>>> rule = Rule("root", "/jobs/job", "+",
...            Rule("title", "./title/text()", "+"),
...            Rule("url", "./url/text()", "+1"),
...            Rule("location", ".", "*",
...                 Rule("country", "./country/text()", "+1"),
...                 Rule("city", "./city/text()", "+1"),
...                 Rule("zip", "./postalcode/text()", "*1")
...            )
...        )

>>> data = parse.xml_type(response.content, rule)
>>> print pretty_json(data)  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
{
        "root": [
            {
                "title": "...",
                "url": "http://importio.applytojob.com/apply/.../...",
                "location": {
                    "country": "United Kingdom",
                    "city": "London",
                    "zip": "EC2M 4YD"
                }
            },
            ...
            {
                "title": "...",
                "url": "http://importio.applytojob.com/apply/.../...",
                "location": {
                    "country": "United Kingdom",
                    "city": "London"
                }
            },
            ...
        ]
    }

test external dsl
-----------------

>>> from ciur import bnf_parser
>>> res = bnf_parser.external2dict(open("ciur.d/import.io_jobs.ciur"))
>>> rule = Rule.from_dict(res[0])  # doctest: +NORMALIZE_WHITESPACE
>>> data = parse.xml_type(response.content, rule)
>>> print pretty_json(data) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
{
        "root": [
            {
                "title": "...",
                "url": "http://importio.applytojob.com/apply/.../...",
                "location": {
                    "country": "United Kingdom",
                    "city": "London",
                    "zip": "EC2M 4YD"
                }
            },
            ...
            {
                "title": "...",
                "url": "http://importio.applytojob.com/apply/.../...",
                "location": {
                    "country": "United Kingdom",
                    "city": "London"
                }
            },
            ...
        ]
    }




>>> res = bnf_parser.to_dict(open("ciur.d/import.io_jobs.ciur"))
>>> rule = Rule.from_dict(res[0])  # doctest: +NORMALIZE_WHITESPACE
>>> data = parse.xml_type(response.content, rule)
>>> print pretty_json(data) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
{
        "root": [
            {
                "title": "...",
                "url": "http://importio.applytojob.com/apply/.../...",
                "location": {
                    "country": "United Kingdom",
                    "city": "London",
                    "zip": "EC2M 4YD"
                }
            },
            ...
            {
                "title": "...",
                "url": "http://importio.applytojob.com/apply/.../...",
                "location": {
                    "country": "United Kingdom",
                    "city": "London"
                }
            },
            ...
        ]
    }



