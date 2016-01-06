"""
This module collects helper functions and classes.
"""

import inspect
import sys

import requests

from ciur import bnf_parser, get_logger
from ciur import parse
from ciur import pretty_json
from ciur.exceptions import CiurBaseException
from ciur import CONF
from ciur.models import Document
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


LOGGER = get_logger(__name__)


def pretty_parse_(ciur_file_or_path,
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

    :param doctype: MIME types to specify the nature of the file currently
        being handled.
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
        ciur_file_path = ciur.path(ciur_file_or_path, called_by_script)

        ciur_file = open(ciur_file_path)

    res = bnf_parser.external2dict(ciur_file, namespace=namespace)
    rule = Rule.from_list(res)

    if req_callback:
        response = req_callback()
    else:
        response = REQ_SESSION.get(url, headers=headers)
        # TODO: set http timeout 10

    if not CONF["IGNORE_WARNING"] and response.headers.get("Etag"):
        sys.stderr.write("[WARN] request.response has Etag. "
                         "TODO: link to documentation\n")

    if not doctype:
        for i_doc_type in dir(parse):
            if i_doc_type.endswith("_type") and i_doc_type.replace(
                    "_type", "") in response.headers["content-type"]:

                doctype = i_doc_type
                break
        else:
            raise CiurBaseException("can not autodetect doc_type `%s`" %
                                    response.headers["content-type"])

    parse_fun = getattr(parse, doctype)

    if not encoding:
        encoding = response.apparent_encoding

    data = parse_fun(ciur.models.Document(
        response.content,
        url=response.url,
        namespace=namespace,
        encoding=encoding
    ), rule[0])

    return pretty_json(data)


def pretty_parse_from_document(ciur_file_or_path, document, doctype="html"):
    """
    WARN:
        do not use this helper in production,
        use only for sake of example,
        because of redundant rules and http session

    :param doctype: MIME types to specify the nature of the file currently
        being handled.
        see http://www.freeformatter.com/mime-types-list.html

    :param req_callback:
    :param ciur_file_or_path: external dsl
    :param url: url to be fetch with GET requests lib
    :return : extracted data as pretty json
    """
    
    ciur_file_path, ciur_file = ciur_file_or_path.name, ciur_file_or_path

    res = bnf_parser.external2dict(ciur_file, namespace=document.namespace)
    rule = Rule.from_list(res)

    parse_fun = getattr(parse, doctype + "_type")

    data = parse_fun(document, rule[0])

    return pretty_json(data)


def pretty_parse_from_url(ciur_file_or_path, url, namespace=None):
    """
    WARN:
        do not use this helper in production,
        use only for sake of example,
        because of redundant rules and http session

    :param doctype: MIME types to specify the nature of the file currently
        being handled.
        see http://www.freeformatter.com/mime-types-list.html

    :param req_callback:
    :param ciur_file_or_path: external dsl
    :param url: url to be fetch with GET requests lib
    :return : extracted data as pretty json
    """

    response = REQ_SESSION.get(url, headers=HTTP_HEADERS)

    doctype = response.headers["content-type"]

    if "/xml" in doctype:
        doctype = "xml"
    elif "/html" in doctype:
        doctype = "html"

    document = Document(
            response.content,
            namespace=namespace
    )

    LOGGER.debug("doctype: `%s`", doctype)

    return pretty_parse_from_document(
        ciur_file_or_path, document,
        doctype=doctype
    )

