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
...            Rule("title", "./title", ["str", "+"]),
...            Rule("url", "./url", ["str", "+1"]),
...            Rule("location", ".", "*",
...                 Rule("country", "./country", ["str", "+1"]),
...                 Rule("city", "./city", ["str", "+1"]),
...                 Rule("zip", "./postalcode", ["str", "*1"])
...            )
...        )

>>> data = parse.xml(response.content, rule)
>>> print pretty_json(data)  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    [
        {
            "title": "...",
            "url": "http://importio.applytojob.com/apply/.../...",
            "location": {
                "location": {
                    "country": "United Kingdom",
                    "city": "London"
                }
            }
        },
        ...
        {
            "title": "Head of Demand Generation",
            "url": "http://importio.applytojob.com/apply/JKlikE/Head-Of-Demand-Generation",
            "location": {
                "location": {
                    "country": "United States",
                    "city": "San Francisco",
                    "zip": "94103"
                }
            }
        },
        ...
    ]


test external dsl
-----------------

>> from ciur import bnf_parser
>> res = bnf_parser.to_dict("import.io_jobs.ciur")
>> rule = Rule.from_dict(res[0])  # doctest: +NORMALIZE_WHITESPACE
>> data = parse.xml(response.content, rule)
>> print pretty_json(data) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    [
        {
            "title": "...",
            "url": "http://importio.applytojob.com/apply/.../...",
            "location": {
                "location": {
                    "country": "United Kingdom",
                    "city": "London"
                }
            }
        },
        ...
        {
            "title": "Head of Demand Generation",
            "url": "http://importio.applytojob.com/apply/JKlikE/Head-Of-Demand-Generation",
            "location": {
                "location": {
                    "country": "United States",
                    "city": "San Francisco",
                    "zip": "94103"
                }
            }
        },
        ...
    ]