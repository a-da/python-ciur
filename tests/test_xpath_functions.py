import re

import pytest

from ciur import bnf_parser, open_file
from ciur.rule import Rule
from requests import Response
from ciur import parse
import ciur.exceptions


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
