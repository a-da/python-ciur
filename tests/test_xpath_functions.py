import re

import pytest
from requests import Response

import ciur.exceptions
from ciur import bnf_parser, parse
from ciur.rule import Rule


def test_replace_bad_regexp():
    ciur_rule = """\
root `/html/body` +1
    replace css `#replace` float replace('**123.0', '321') +1
"""
    test_html = """
    <html>
        <body>
            <ul>
                <li id='replace'>123</li>
            </ul>
        </body>
    </html>
    """.encode()

    res = bnf_parser.external2dict(ciur_rule)
    response = Response()
    response._content = test_html
    response.headers['content-type'] = "text/html"

    rule = Rule.from_dict(res[0])
    with pytest.raises(ciur.exceptions.CiurBaseException,
                       match=re.escape(r", wrong regexp-> nothing to repeat at "
                                       r"position 0 `**123.0`")) as e:
        parse.html_type(parse.Document(response), rule)


def test_url_functions():
    html_document = parse.Document(
        content="""
        <html>
            <body>
                <ul>
                    <li id='url_param'>http://some-web-site?some-param=some-value</li>
                     <li id='url'>relative/path</li>
                </ul>
            </body>
        </html>
        """,
        url="http://some-web-site?some-param=some-value"
    )

    rule_definition = "\n".join((
        "",
        "body `//body` +1",
        "    url_param css `#url_param` text url_param('some-param') +1",
        "    url css `#url` text url +1",
        ""))

    rule = Rule.from_dsl(rule_definition)[0]

    result = parse.html_type(html_document, rule)

    assert result['body']['url_param'] == 'some-value'
    assert result['body']['url'] == 'http://some-web-site/relative/path'
