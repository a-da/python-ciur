# -*- coding: utf-8 -*-
"""
basic function for casting or type conversion/transformation

NOTE:
    local convention for all public cast function is `[a-z]+[a-z0-9_]+_` it should end with underscore
"""
import HTMLParser
import urlparse

# noinspection PyProtectedMember
from lxml.etree import _Element as EtreeElement

from lxml.etree import tostring
from dateutil import parser
from ciur.exceptions import CiurBaseException
from ciur.dateutil_aditional_languages import MONTHS


def element2text(value):
    """
    convert value to text if is EtreeElement or strip value is is text already
    :param value:
        :type value: EtreeElement or list or str
    :rtype str
    """
    if isinstance(value, EtreeElement):
        return value.text
    elif isinstance(value, list) and len(value) > 0:
        return [element2text(i) for i in value]

    if not value:
        return value

    return value.strip()


def url_(url, base_url):
    """
    get absolute url
    """
    return urlparse.urljoin(base_url, url)


def url_param_(url, param, *_):
    """
    get param from url
    """
    parsed = urlparse.urlparse(url)
    return urlparse.parse_qs(parsed.query)[param]


def int_(value, *_):
    """
    convert data into integer
    :rtype: int
    """
    return int(value)


def float_(value, *_):
    """
    convert data into integer
    :rtype: int
    """
    text = element2text(value)
    if text == "":
        return text

    try:
        return float(text)
    except (ValueError,) as value_error:
        if "invalid literal for float()" in value_error.message:
            return float(text.replace(",", "."))
        else:
            raise value_error


def raw_(value, *_):
    """
    get raw representation of DOM
    :param value:
        :type value: EtreeElement or basestring
    :param _: unused args
    """
    if isinstance(value, basestring):
        return value

    return HTML_PARSER.unescape(tostring(value))


def iraw_(value, *_):
    """
    get raw representation of children DOM aka innerHTML
    :param value:
        :type value: EtreeElement or basestring
    :param _: unused args
    """
    text = value.text.strip() if value.text else ""
    tail = value.tail.strip() if value.tail else ""
    if tail:
        tail = " " + tail

    return text + "".join(raw_(child) for child in value) + tail


def size_(got, mandatory_or_optional, expect):
    """
    check if expected size match result size
    """
    if mandatory_or_optional == "mandatory":
        if not got:  # + got 0
            assert False, "expect mandatory"
        elif expect is 0:  # +0 got 1
            pass
        else:  # +10 got 1
            assert got == expect, "expect size `%s`, got `%s`" % (expect, got)
    else:
        if not got:  # * got 0
            pass
        elif expect is 0:  # * got 19
            pass
        else:  # *5 got 5
            assert got == expect, "expect size `%s`, got `%s`" % (expect, got)


def datetime_(value):
    """
    because of exception (bellow) string do datetime CAN NOT be embedded into lxml namespace functions
        File "extensions.pxi", line 612, in lxml.etree._wrapXPathObject (src/lxml/lxml.etree.c:145847)
        lxml.etree.XPathResultError: Unknown return type: datetime.datetime

    So this is the reason why it is implemented in type_list casting chain
    """
    text = element2text(value)

    if not text:
        return value

    for foreign, english in MONTHS.iteritems():
        text = text.replace(foreign, english)

    try:
        return parser.parse(text)
    except (ValueError,) as value_error:
        raise CiurBaseException(value_error, {"text": text})


def tail_(value):
    """
    >> xpath(<div><p>paragraph</p>tail_text</div>).tail
    tail_text

    :param value:
        :type value: EtreeElement or basestring
    :rtype str
    """
    return value.tail


HTML_PARSER = HTMLParser.HTMLParser()
