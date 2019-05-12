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
    long_chain1 css `#long_chain1` replace('x', '') replace('y', '') dehumanise_number decimal +1
    long_chain22 css `#long_chain2` replace('N/A', '0') float *1
    long_chain2 css `#long_chain2` replace('N/A', '0') float decimal *1
"""
    test_html = """
<html>
    <body>
        <ul>
            <li id='decimal'>69.69</li>
            <li id='built_in'>not-Capitalised</li>
            <li id='long_chain1'>x69kxy</li>
            <li id='long_chain2'>0</li>
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
    assert data['root']['long_chain1'] == Decimal('69000.0')
    assert data['root'].get('long_chain2') == Decimal('0')
