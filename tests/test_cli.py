from pathlib import Path
from unittest import mock
from textwrap import dedent

import pytest

import ciur  # just for mock
import sys  # just for mock
import platform  # just for mock

from ciur.cli import VERSION_STRING

with \
        mock.patch.object(
            sys, "argv", 
            new_callable=mock.PropertyMock(return_value=["ciur"])), \
        mock.patch.object(
            ciur, "VERSION",
            new_callable=mock.PropertyMock(return_value="0.2.0")), \
        mock.patch.object(platform, "release",
                          return_value="5.4.1-64-generic"):
    
    from ciur import cli


EXAMPLE_ORG = """{
    "root": {
        "name": "Example Domain",
        "paragraph": "This domain is for use in illustrative examples in documents. You may use this\\n    domain in literature without prior coordination or asking for permission."
    }
}"""

EXAMPLE_ORG_CIUR_AS_URL = "https://some.domain/example.org.ciur"


@pytest.mark.parametrize("test_input,expected", [
    (
        ("--version",),
        VERSION_STRING
    ),
    (
        ("--help",),

        dedent("""\
        usage: ciur [-h] -p PARSE -r RULE [-w] [-v]

        *Ciur is a scrapper layer based on DSL for extracting data*

        *Ciur is a lib because it has less black magic than a framework*

        If you are annoyed by `Spaghetti code` then we can taste `Lasagna code`
        with the help of Ciur

        options:
          -h, --help         show this help message and exit
          -p, --parse PARSE  url or local file path required document for html, xml, pdf. (f.e. http://example.org or /tmp/example.org.html)
          -r, --rule RULE    url or local file path file with parsing dsl rule (f.e. /tmp/example.org.ciur or http:/host/example.org.ciur)
          -w, --ignore_warn  suppress python warning warnings and ciur warnings hints
          -v, --version      show program's version number and exit
        """)
        # "usage: ciur ", "usage: _jb_pytest_runner.py "
    )
])
def test_cli_parse_basic(capfd, test_input, expected):
    
    with \
            pytest.raises(SystemExit) as exc_info:
        
        cli.parse_cli(*test_input)

    assert exc_info.value.code == 0

    out, err = capfd.readouterr()
    assert out.strip() == expected.strip() #, (err, out.strip())


@pytest.mark.parametrize("test_input,expected", [
    pytest.param(
        (
            "--parse", "http://example.org",
            "--rule", EXAMPLE_ORG_CIUR_AS_URL,
        ),
        EXAMPLE_ORG,
        id='url-url',
    ),
    pytest.param(
        (
            "--parse", "./res/example.org.html",
            "--rule", "./res/example.org.ciur",
        ),
        EXAMPLE_ORG,
        id='local-local',
    ),
    pytest.param(
        (
            "--parse", "http://example.org",
            "--rule", "./res/example.org.ciur",
        ),
        EXAMPLE_ORG,
        id='url-local',
    ),
    pytest.param(
        (
            "--parse", "./res/example.org.html",
            "--rule", EXAMPLE_ORG_CIUR_AS_URL
        ),
        EXAMPLE_ORG,
        id='local-url'
    ),
])
def test_cli_parse_resources(test_input, expected):
    """
    parse url and local combinations
    """
    # WHEN
    with mock.patch('ciur.shortcuts.REQ_SESSION') as req_session:
        req_session.get.return_value.text = (
            Path(__file__).parent / 'res/example.org.ciur'
        ).read_text()
        
        result = cli.parse_cli(*test_input)
    
    # THEN
    assert result == expected


@pytest.mark.parametrize("test_input,expected", [
    pytest.param(
        (
            "--parse", "./res/example.org",
            "--no-rule", "./res/example.org.ciur",
        ),
        "error: argument -p/--parse: "
        "[Errno 2] No such file or directory: './res/example.org'",
        id="no-rule",
    ),
    pytest.param(
        (
            "--no-parse", "./res/example.org",
            "--rule", "./res/example.org.ciur",
        ),
        "error: the following arguments are required: -p/--parse",
        id="no-parse",
    ),
    pytest.param(
        (
            "--no-parse", "./res/example.org",
            "--no-rule", "./res/example.org.ciur",
        ),
        "error: the following arguments are required: -p/--parse",
        id="no-parse-no-rule",
    ),
])
def test_cli_parse_fails(capfd, test_input, expected):
    """
    parse url and files
    """
    with pytest.raises(SystemExit) as exc_info:
        cli.parse_cli(*test_input)

    assert exc_info.value.code == 2

    out, err = capfd.readouterr()
    assert expected in err

