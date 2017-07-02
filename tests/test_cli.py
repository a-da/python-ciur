import pytest

from ciur import cli

HELP = """\
usage: ciur [-h] -p PARSE -r RULE [-w IGNORE_WARN] [-v]

*Ciur is a scrapper layer*

*Ciur is a lib because it has less black magic than a framework*

If you are annoyed by `Spaghetti code` than we can taste `Lasagna code`
with help of Ciur

https://bitbucket.org/ada/python-ciur

optional arguments:
  -h, --help            show this help message and exit
  -p PARSE, --parse PARSE
                        url or local file path required document for html, xml, pdf. (f.e. http://example.org or /tmp/example.org.html)
  -r RULE, --rule RULE  url or local file path file with parsing dsl rule (f.e. /tmp/example.org.ciur or http:/host/example.org.ciur)
  -w IGNORE_WARN, --ignore_warn IGNORE_WARN
                        suppress warning
  -v, --version         show program's version number and exit
"""

EXAMPLE_ORG = """{
    "root": {
        "name": "Example Domain",
        "paragraph": "This domain is established to be used for illustrative examples in documents. You may use this\\n    domain in examples without prior coordination or asking for permission."
    }
}"""

EXAMPLE_ORG_CIUR_AS_URL = "https://bitbucket.org/ada/python-ciur/raw/HEAD/docs/docker/example.org.ciur"


@pytest.mark.parametrize("test_input,expected", [
    (
        ("--version",),
        "ciur/0.1.2 Python/3.6.1 Linux/4.4.0-21-generic\n".replace(
            "ciur/", "_jb_pytest_runner.py/")
    ),
    (
         ("--help",), HELP.replace(
            "usage: ciur ", "usage: _jb_pytest_runner.py ")
    )
])
def test_cli_parse_basic(capfd, test_input, expected):

    with pytest.raises(SystemExit) as exc_info:
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

