"""
This module collects helper functions and classes.
"""

import requests

from ciur import bnf_parser, parse, pretty_json, CiurException
from ciur.rule import Rule

requests = requests.Session()


def pretty_parse(ciur_file_path, url, doctype=None, namespace=None):
    """
    WARN:
        do not use this helper in production,
        use only for sake of example,
        because of redundant rules and http session

    :param ciur_file_path: external dsl
    :param url: url to be fetch with GET requests lib
    :return : extracted data as pretty json
    """

    # workaround for get relative files
    import os
    import inspect
    called_by_script = inspect.stack()[1][1]
    ciur_file_path = os.path.join(os.path.dirname(called_by_script), ciur_file_path)

    res = bnf_parser.to_dict(open(ciur_file_path), namespace=namespace)
    rule = Rule.from_list(res)
    response = requests.get(url)

    if not doctype:
        if "xml" in response.headers["content-type"]:
            doctype = "xml"
        elif "html" in response.headers["content-type"]:
            doctype = "html"
        else:
            raise CiurException("can not autodetect doctype `%s`" % response.headers["content-type"])

    parse_fun = getattr(parse, doctype)

    data = parse_fun(response.content, rule[0], url=response.url, namespace=namespace)

    return pretty_json(data)
