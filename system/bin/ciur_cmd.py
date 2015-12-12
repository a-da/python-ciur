#!/usr/bin/env python

import argparse
import sys


from requests.models import PreparedRequest
import requests.exceptions

import ciur
from ciur.shortcuts import pretty_parse


parser = argparse.ArgumentParser(description=ciur.__doc__)


def check_url(url):
    prepared_request = PreparedRequest()
    try:
        prepared_request.prepare_url(url, None)
        return prepared_request.url
    except requests.exceptions.MissingSchema, e:
        raise argparse.ArgumentTypeError(e)


def check_file(path):
    if not path.endswith(".ciur"):
        sys.stderr.write("[WARN] is recommended that rule files have extension `.ciur`\n\n")

    try:
        return open(path)
    except IOError, e:
        raise argparse.ArgumentTypeError(e)


parser.add_argument("-u",
                    "--url",
                    required=True,
                    help="url of required document html, xml, pdf. \n (f.e. http://example.com)",
                    type=check_url
                    )

parser.add_argument("-r", "--rule",
                    required=True,
                    help='file with rule (f.e. /tmp/example.com.ciur)',
                    type=check_file
                    )

parser.add_argument("-w", "--ignore_warn",
                    help='suppress warning',
                    type=bool
                    )

args = parser.parse_args()

if args.ignore_warn:
    ciur.CONF["IGNORE_WARNING"] = args.ignore_warn

print pretty_parse(args.rule, args.url)







