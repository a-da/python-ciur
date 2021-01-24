Testing http://example.org
==========================
>>> import os

>>> from ciur import parse, pretty_json
>>> from ciur.rule import Rule
>>> import requests

>>> requests = requests.Session()
>>> response = requests.get("http://example.org")

test internal dsl
-----------------

>>> rule = Rule("root", "/html/body", "+1",
...              Rule("name", ".//h1/text()", ["+1"]),
...              Rule("paragraph", ".//p/text()", ["+1"])
... )

>>> data = parse.html_type(parse.Document(response.content), rule)
>>> print(pretty_json(data))  # doctest: +NORMALIZE_WHITESPACE
{
    "root": {
        "name": "Example Domain",
        "paragraph": "This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission."
    }
}

test external dsl
-----------------

>>> from ciur import bnf_parser, open_file

>>> import pathlib
>>> # str(pathlib.Path(bnf_parser.__file__).parent.parent)

>>> res = bnf_parser.external2dict(open_file(
...     "../tests/res/example.org.ciur"
... ))
>>> rule = Rule.from_dict(res[0])  # doctest: +NORMALIZE_WHITESPACE
>>> data = parse.html_type(parse.Document(response.content), rule)
>>> print(pretty_json(data))  # doctest: +NORMALIZE_WHITESPACE
{
    "root": {
        "name": "Example Domain",
        "paragraph": "This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission."
    }
}

>>> res = bnf_parser.external2dict(open_file(
...     "../tests/res/example.org.ciur"
... ))
>>> rule = Rule.from_dict(res[0])  # doctest: +NORMALIZE_WHITESPACE
>>> data = parse.html_type(parse.Document(response.content), rule)
>>> print(pretty_json(data))  # doctest: +NORMALIZE_WHITESPACE
{
    "root": {
        "name": "Example Domain",
        "paragraph": "This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission."
    }
}

>>> res = bnf_parser.external2dict(open_file(
...     "../tests/res/example.org.ciur"
... ))
>>> rule = Rule.from_dict(res[0])  # doctest: +NORMALIZE_WHITESPACE
>>> data = parse.html_type(parse.Document(response.content), rule)
>>> print(pretty_json(data))  # doctest: +NORMALIZE_WHITESPACE
{
    "root": {
        "name": "Example Domain",
        "paragraph": "This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission."
    }
}
