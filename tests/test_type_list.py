from ciur import bnf_parser, open_file
from ciur.rule import Rule
from unittest.mock import MagicMock
from requests import Response
from ciur import parse, pretty_json
from decimal import Decimal


def test_type_casting():
    ciur_rule = """\
root `/html/body` +1
    decimal css `#decimal` decimal +1
    built_in css `#built_in` text str.capitalize +1
"""
    test_html = """
<html>
    <body>
        <ul>
            <li id='decimal'>69.69</li>
            <li id='built_in'>not-Capitalised</li>
        </ul>
    </body>
</html>
""".encode()

    res = bnf_parser.external2dict(ciur_rule)
    response = Response()
    response._content = test_html
    response.headers['content-type'] = "text/html"

    rule = Rule.from_dict(res[0])
    data = parse.html_type(parse.Document(response), rule)

    assert data['root']['decimal'] == Decimal('69.69')
    assert data['root']['built_in'] == "Not-capitalised"
