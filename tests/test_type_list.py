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
    long_chain_float css `#long_chain2` replace('N/A', '10') float *1
    long_chain_decimal  css `#long_chain2` replace('N/A', '20') float decimal *1
    list css `#list > i` replace('10', '30') float decimal +2
    replace css `#replace` replace('something', '') *
    replace_not_string css `#replace_not_string` float replace('123.0', '321') +1
    no_matches css `#replace` matches('[0-9]+') *
    matches css `#list > i` matches('[0-9]+') text *
"""
    test_html = """
<html>
    <body>
        <ul>
            <li id='decimal'>69.69</li>
            <li id='built_in'>not-Capitalised</li>
            <li id='long_chain1'>x69kxy</li>
            <li id='long_chain2'>90</li>
            <li id='list'><i>10</i>><i>20</i></li>
            <li id='replace'></li>
            <li id='replace_not_string'>123</li>
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
    assert data['root'].get('long_chain_float') == 90.0
    assert data['root'].get('long_chain_decimal') == Decimal('90')
    assert data['root'].get('list') == [Decimal('30.0'), Decimal('20.0')]
    assert data['root'].get('replace') is None
    assert data['root'].get('no_matches') is None
    assert data['root'].get('matches') == ['10', '20']
