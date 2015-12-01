"""
This module collects helper functions and classes.
"""

import requests
import os
import inspect

from ciur import bnf_parser, parse, pretty_json, CiurException
from ciur.rule import Rule
import ciur

req_session = requests.Session()

_HTTP_HEADERS = {
    "User-Agent": "%s/%s %s/%s %s" % (
        ciur.__title__, ciur.__version__,
        requests.__title__, requests.__version__,

        ciur.__git__
    )
}


def pretty_parse(ciur_file_path, url, doctype=None, namespace=None, headers=_HTTP_HEADERS, encoding=None):
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
    called_by_script = inspect.stack()[1][1]
    ciur_file_path = os.path.join(os.path.dirname(called_by_script), ciur_file_path)

    res = bnf_parser.to_dict(open(ciur_file_path), namespace=namespace)
    rule = Rule.from_list(res)
    response = req_session.get(url, headers=headers)

    if response.headers.get("Etag"):
        import sys
        sys.stderr.write("[WARN] request.response has Etag")

    if not doctype:
        for i_doc_type in dir(parse):
            if i_doc_type.endswith("_type") and i_doc_type.replace("_type", "") in response.headers["content-type"]:
                doctype = i_doc_type
                break
        else:
            raise CiurException("can not autodetect doc_type `%s`" % response.headers["content-type"])

    parse_fun = getattr(parse, doctype)

    if not encoding:
        encoding = response.apparent_encoding
    data = parse_fun(response.content, rule[0], url=response.url, namespace=namespace, encoding=encoding)

    return pretty_json(data)
