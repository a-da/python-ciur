from unittest import mock
from textwrap import dedent

import pytest

import ciur  # just for mock
import sys  # just for mock
import platform  # just for mock


with \
        mock.patch.object(
            sys, "argv", 
            new_callable=mock.PropertyMock(return_value=["ciur"])), \
        mock.patch.object(
            ciur, "__version__",
            new_callable=mock.PropertyMock(return_value="0.2.0")):
    
    from ciur import cli


EXAMPLE_ORG = """{
    "root": {
        "name": "Example Domain",
        "paragraph": "This domain is for use in illustrative examples in documents. You may use this\\n    domain in literature without prior coordination or asking for permission."
    }
}"""

EXAMPLE_ORG_CIUR_AS_URL = "https://bitbucket.org/ada/python-ciur/raw/HEAD/docs/docker/example.org.ciur"


@pytest.mark.parametrize("test_input,expected", [
    (
        ("--version",),
        "ciur/0.2.0 Python/3.9.1 Linux/5.4.0-64-generic\n"
    ),
    (
        ("--help",),

        dedent("""\
        usage: ciur [-h] -p PARSE -r RULE [-w] [-v]

        *Ciur is a scrapper layer based on DSL for extracting data*

        *Ciur is a lib because it has less black magic than a framework*

        If you are annoyed by `Spaghetti code` than we can taste `Lasagna code`
        with help of Ciur

        https://bitbucket.org/ada/python-ciur

        optional arguments:
          -h, --help            show this help message and exit
          -p PARSE, --parse PARSE
                                url or local file path required document for html, xml, pdf. (f.e. http://example.org or /tmp/example.org.html)
          -r RULE, --rule RULE  url or local file path file with parsing dsl rule (f.e. /tmp/example.org.ciur or http:/host/example.org.ciur)
          -w, --ignore_warn     suppress python warning warnings and ciur warnings hints
          -v, --version         show program's version number and exit
        """)
        # "usage: ciur ", "usage: _jb_pytest_runner.py "
    )
])
def test_cli_parse_basic(capfd, test_input, expected):
    
    with \
            pytest.raises(SystemExit) as exc_info, \
            mock.patch.object(platform, "release", 
                              return_value="5.4.0-64-generic"):
        
        cli.parse_cli(*test_input)

    assert exc_info.value.code == 0

    out, err = capfd.readouterr()
    assert out == expected, err


@pytest.mark.parametrize("test_input,expected", [
    (
        (
            "--parse", "http://example.org",
            "--rule", EXAMPLE_ORG_CIUR_AS_URL,
        ),
        EXAMPLE_ORG,
    ),
    (
        (
            "--parse", "./res/example.org.html",
            "--rule", "./res/example.org.ciur",
        ),
        EXAMPLE_ORG,
    ),
    (
        (
            "--parse", "http://example.org",
            "--rule", "./res/example.org.ciur",
        ),
        EXAMPLE_ORG,
    ),
    (
        (
            "--parse", "./res/example.org.html",
            "--rule", EXAMPLE_ORG_CIUR_AS_URL
        ),
        EXAMPLE_ORG,
    ),
    # (
    #     # use file sources
    #     (
    #         "--parse", "./res/example.org",
    #         "--no-rule", "./res/example.org.ciur",
    #     ),
    #     """dsdsds"""
    # ),
])
def test_cli_parse_resources(test_input, expected):
    """
    parse url and files
    """
    assert cli.parse_cli(*test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    (
        (
            "--parse", "./res/example.org",
            "--no-rule", "./res/example.org.ciur",
        ),
        "error: argument -p/--parse: "
        "[Errno 2] No such file or directory: './res/example.org'"
    ),
    (
        (
            "--no-parse", "./res/example.org",
            "--rule", "./res/example.org.ciur",
        ),
        "error: the following arguments are required: -p/--parse"
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

