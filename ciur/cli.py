#!/usr/bin/env python
"""
>>> import os

Success test
~~~~~~~~~~~~

>>> parse_cli(
... "--url", "http://example.org",
... "--rule", os.path.join(ciur.__path__[0], "..", "tests/ciur.d/example.com.ciur"),
... "--ignore_warn", "true",
... ) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
{
    "root": {
        "name": "Example Domain",
        "paragraph": "This domain is established to be used for illustrative examples in documents. You may use this\\n    domain in examples without prior coordination or asking for permission."
    }
}

Fail bad url argument
~~~~~~~~~~~~~~~~~~~~~

>>> parse_cli(
... "--url", "example.org",
... )
Traceback (most recent call last):
...
SystemExit: 2



"""
import argparse
import sys


from requests.models import PreparedRequest
import requests.exceptions

import ciur
from ciur.shortcuts import pretty_parse


def check_url(url):
    prepared_request = PreparedRequest()
    try:
        prepared_request.prepare_url(url, None)
        return prepared_request.url
    except (requests.exceptions.MissingSchema,) as url_error:
        raise argparse.ArgumentTypeError(url_error)


def check_file(path):
    if not path.endswith(".ciur"):
        sys.stderr.write("[WARN] is recommended that rule files have extension `.ciur`\n\n")

    try:
        return open(path)
    except (IOError, ) as io_error:
        raise argparse.ArgumentTypeError(io_error)


PARSER = argparse.ArgumentParser(description=ciur.__doc__)

PARSER.add_argument(
    "-u",
    "--url",
    required=True,
    help="url of required document html, xml, pdf. \n (f.e. http://example.com)",
    type=check_url
)

PARSER.add_argument(
    "-r",
    "--rule",
    required=True,
    help='file with rule (f.e. /tmp/example.com.ciur)',
    type=check_file
)

PARSER.add_argument(
    "-w", "--ignore_warn",
    help='suppress warning',
    type=bool
)


def parse_cli(*argv):
    args = PARSER.parse_args(argv)

    if args.ignore_warn:
        ciur.CONF["IGNORE_WARNING"] = args.ignore_warn

    print pretty_parse(args.rule, args.url)
    
    
if __name__ == "__main__":
    parse_cli(*sys.argv)

    # TODO: use also stream
    # bash$ curl "http://example.org" | ciur --rule=/tmp/example.org.ciur
    # if len(sys.argv) > 1:
    #     parse_cli(sys.argv[1])
    # else:
    #     # parse_cli(sys.stdin.readline, sys.argv[1])
    #     pass
