#!/usr/bin/env python
"""
Command line interface for ``ciur`` module.

Test on python level
====================

Success test
~~~~~~~~~~~~

>>> parse_cli(
... "--url", "http://example.org",
... "--rule", ciur.path("../tests/ciur.d/example.org.ciur"),
... "--ignore_warn", "true",
... ) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
{
    "root": {
        "name": "Example Domain",
        "paragraph": "This domain is established to be used for illustrative
        examples in documents. You may use this\\n domain in examples without
        prior coordination or asking for permission."
    }
}

Test on shell level
===================

    Command: Help
    -------------

    More about of reason to use ``sh``
    http://stackoverflow.com/questions/34266190/
    cover-cli-py-file-python-argparse-with-doctest
    >>> import sh

    >>> python = sh.Command(sys.executable)
    >>> python(__file__, "--help")
    ... # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    usage: cli.py... [-h] -u URL -r RULE [-w IGNORE_WARN]
    *Ciur is a scrapper layer*
    ...
    optional arguments:
      -h, --help            show this help message and exit
      -u URL, --url URL     url of required document html, xml, pdf. (f.e.
                            http://example.org)
      -r RULE, --rule RULE  file with rule (f.e. /tmp/example.org.ciur)
      -w IGNORE_WARN, --ignore_warn IGNORE_WARN
                            suppress warning

    Url validation
    --------------

    >>> python(__file__, "--url", "example.org")
    ... # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    Traceback (most recent call last):
      ...
    sh.ErrorReturnCode_2: 
        RAN: '.../bin/python... .../ciur/cli.py --url example.org'
        STDOUT:
        STDERR:
    usage: cli.py... [-h] -u URL -r RULE [-w IGNORE_WARN]
    cli.py...: error: argument -u/--url: Invalid URL 'example.org': 
        No schema supplied. Perhaps you meant http://example.org?

"""
import argparse
from argparse import RawTextHelpFormatter
import sys
import os

from requests.models import PreparedRequest
import requests.exceptions

try:
    import ciur
    from ciur.shortcuts import pretty_parse_from_url
except (ImportError,) as import_error:
    # work around for `No module named ciur`
    # TODO make it logging
    # print e
    sys.path.append(os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    ))

    import ciur
    from ciur.shortcuts import pretty_parse_from_url


def check_url(url):
    """
    :param url:
        :type url: str
    """
    prepared_request = PreparedRequest()
    try:
        prepared_request.prepare_url(url, None)
        return prepared_request.url
    except (requests.exceptions.MissingSchema,) as url_error:
        raise argparse.ArgumentTypeError(url_error)


def check_file(path):
    """
    :param path:
        :type path: str
    """
    if not path.endswith(".ciur"):
        sys.stderr.write("[WARN] is recommended that rule files have"
                         "extension `.ciur`\n\n")

    try:
        return open(path)
    except (IOError, ) as io_error:
        raise argparse.ArgumentTypeError(io_error)


PARSER = argparse.ArgumentParser(
    description=ciur.__doc__,
    formatter_class=RawTextHelpFormatter
)


PARSER.add_argument(
    "-u",
    "--url",
    required=True,
    help="url of required document html, xml, pdf."
         " (f.e. http://example.org)",
    type=check_url
)

PARSER.add_argument(
    "-r",
    "--rule",
    required=True,
    help='file with rule (f.e. /tmp/example.org.ciur)',
    type=check_file
)

PARSER.add_argument(
    "-w", "--ignore_warn",
    help='suppress warning',
    type=bool
)


def parse_cli(*argv):
    """
    :param argv: command line arguments
      :type argv: list[str]
    """
    args = PARSER.parse_args(argv)

    if args.ignore_warn:
        ciur.CONF["IGNORE_WARNING"] = args.ignore_warn

    print(pretty_parse_from_url(args.rule, args.url))


def main():
    parse_cli(*sys.argv[1:])


if __name__ == "__main__":    
    parse_cli(*sys.argv[1:])

    # TODO: use also stream
    # bash$ curl "http://example.org" | ciur --rule=/tmp/example.org.ciur
    # if len(sys.argv) > 1:
    #     parse_cli(sys.argv[1])
    # else:
    #     # parse_cli(sys.stdin.readline, sys.argv[1])
    #     pass
