Testing http://import.io/~ourjobs
=================================

>>> from ciur import parse, pretty_json, bnf_parser
>>> from ciur.rule import Rule
>>> from ciur.models import Document

>>> xml_document = Document("""<?xml version="1.0" encoding="UTF-8"?>
... <jobs>
...     <job>
...         <title>Back End Developer</title>
...         <url>http://importio.applytojob.com/apply/.../...</url>
...         <country>United Kingdom</country>
...         <city>London</city>
...         <postalcode>EC2M 4YD</postalcode>
...     </job>
...     <job>
...         <title>Product Manager</title>
...         <url>http://importio.applytojob.com/apply/.../...</url>
...         <country>United Kingdom</country>
...         <city>London</city>
...     </job>
... </jobs>
... """)


test internal dsl
-----------------

>>> rule = Rule("root", "/jobs/job", "+",
...            Rule("title", "./title/text()", "+"),
...            Rule("url", "./url/text()", "+1"),
...            Rule("location", ".", "*",
...                 Rule("country", "./country/text()", "*1"),
...                 Rule("city", "./city/text()", "+1"),
...                 Rule("zip", "./postalcode/text()", "*1")
...            )
...        )

>>> data = parse.xml_type(xml_document, rule)
>>> pretty_data = pretty_json(data)
>>> print(pretty_data) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    {
        "root": [
            {
                "title": "Back End Developer",
                "url": "http://importio.applytojob.com/apply/.../...",
                "location": {
                    "country": "United Kingdom",
                    "city": "London",
                    "zip": "EC2M 4YD"
                }
            },
            {
                "title": "Product Manager",
                "url": "http://importio.applytojob.com/apply/.../...",
                "location": {
                    "country": "United Kingdom",
                    "city": "London"
                }
            }
        ]
    }

test external dsl
-----------------

>>> res = bnf_parser.external2dict("""\
... root `/jobs/job` +
...     title `./title/text()` +
...     url `./url/text()` +1
...     location `.` *
...         country `./country/text()` +1
...         city `./city/text()` +1
...         zip `./postalcode/text()` *1
... """)
>>> rule = Rule.from_dict(res[0])
>>> data == parse.xml_type(xml_document, rule) # look to above representation of data
True
