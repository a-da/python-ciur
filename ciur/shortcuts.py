"""
This module collects helper functions and classes.
"""

import requests

from ciur import bnf_parser, parse, pretty_json
from ciur.rule import Rule

requests = requests.Session()


def pretty_parse(ciur_file_path, url):
    """
    WARN:
        do not use this helper in production,
        use only for sake of example,
        because of redundant rules and http session

    :param ciur_file_path: external dsl
    :param url: url to be fetch with GET requests lib
    :return : extracted data as pretty json
    """
    res = bnf_parser.to_dict(open(ciur_file_path))
    rule = Rule.from_list(res)
    response = requests.get(url)
    data = parse.html(response.content, rule[0], url=response.url)
    return pretty_json(data)
