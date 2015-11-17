# -*- coding: utf-8 -*-
"""
basic function for casting or type conversion/transformation
"""
import HTMLParser
import urlparse

from lxml.etree import tostring
from dateutil import parser

from ciur import CiurException


def url_(url, base_url):
    """
    get absolute url
    """
    return urlparse.urljoin(base_url, url)


def int_(value, *args):
    """
    convert data into integer
    :rtype: int
    """
    return int(value)


def raw_(value, *args):
    """
    get raw representation of DOM
    :param value: etree dom
    """
    return HTML_PARSER.unescape(tostring(value))


def iraw_(value, *args):
    """
    get raw representation of children DOM aka innerHTML
    :param value: etree dom
    """
    return value.text + "".join(raw_(child) for child in value) + value.tail


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


def datetime_(text):
    """
    because of exception (bellow) string do datetime CAN NOT be embedded into lxml namespace functions
        File "extensions.pxi", line 612, in lxml.etree._wrapXPathObject (src/lxml/lxml.etree.c:145847)
        lxml.etree.XPathResultError: Unknown return type: datetime.datetime

    So this is the reason why it is implemented in type_list casting chain
    """
    if not text:
        return text

    # workaround http://stackoverflow.com/questions/8896038/how-to-use-python-dateutil-1-5-parse-function-to-work-with-unicode
    languages = {
        "russian": {
            u"Янв": "January",
            u"Февр": "February",
            u"Март": "March",
            u"Апр": "April",
            u"Май": "May",
            u"Июнь": "June",
            u"Июль": "July",
            u"Авг": "August",
            u"Сент": "September",
            u"Окт": "October",
            u"Нояб": "November",
            u"Дек": "December"
        },
        "romanian": {
            "ianuarie": "January",
            "februarie": "February",
            "martie": "March",
            "aprilie": "April",
            "mai": "May",
            "iunie": "June",
            "iulie": "July",
            "august": "August",
            "septembrie": "September",
            "octombrie": "October",
            "noiembrie": "November",
            "decembrie": "December"
        }
    }

    for lang_i in languages.values():
        for k, v in lang_i.iteritems():
            text = text.replace(k.lower(), v)
            text = text.replace(k.upper(), v)
            text = text.replace(k.capitalize(), v)

    try:
        return parser.parse(text)
    except ValueError, e:
        raise CiurException(e, {"text": text})


HTML_PARSER = HTMLParser.HTMLParser()
