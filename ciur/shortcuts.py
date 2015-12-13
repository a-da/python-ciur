"""
This module collects helper functions and classes.
"""

import os
import inspect
import sys

import requests

from ciur import bnf_parser
from ciur import parse
from ciur import pretty_json
from ciur.exceptions import CiurBaseException
from ciur import CONF
from ciur.rule import Rule
import ciur

REQ_SESSION = requests.Session()

HTTP_HEADERS = {
    "User-Agent": "%s/%s %s/%s %s" % (
        ciur.__title__, ciur.__version__,
        requests.__title__, requests.__version__,

        ciur.__git__
    )
}


def pretty_parse(ciur_file_or_path,
                 url,
                 doctype=None,
                 namespace=None,
                 headers=None,
                 encoding=None,
                 req_callback=None):
    """
    WARN:
        do not use this helper in production,
        use only for sake of example,
        because of redundant rules and http session

    :param doctype: MIME types to specify the nature of the file currently being handled.
        see http://www.freeformatter.com/mime-types-list.html

    :param req_callback:
    :param ciur_file_or_path: external dsl
    :param url: url to be fetch with GET requests lib
    :return : extracted data as pretty json
    """
    if not headers:
        headers = HTTP_HEADERS

    # workaround for get relative files
    called_by_script = inspect.stack()[1][1]

    if isinstance(ciur_file_or_path, file):
        ciur_file_path, ciur_file = ciur_file_or_path.name, ciur_file_or_path
    else:
        ciur_file_path = os.path.join(os.path.dirname(called_by_script), ciur_file_or_path)
        ciur_file = open(ciur_file_path)

    res = bnf_parser.to_dict(ciur_file, namespace=namespace)
    rule = Rule.from_list(res)

    if req_callback:
        response = req_callback()
    else:
        response = REQ_SESSION.get(url, headers=headers)
        # TODO: set http timeout 10

    if not CONF["IGNORE_WARNING"] and response.headers.get("Etag"):
        sys.stderr.write("[WARN] request.response has Etag. TODO: link to documentation\n")

    if not doctype:
        for i_doc_type in dir(parse):
            if i_doc_type.endswith("_type") and i_doc_type.replace("_type", "") in response.headers["content-type"]:
                doctype = i_doc_type
                break
        else:
            raise CiurBaseException("can not autodetect doc_type `%s`" % response.headers["content-type"])

    parse_fun = getattr(parse, doctype)

    if not encoding:
        encoding = response.apparent_encoding
    data = parse_fun(response.content, rule[0], url=response.url, namespace=namespace, encoding=encoding)

    return pretty_json(data)
