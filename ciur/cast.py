"""
basic function for casting or type conversion/transformation
"""
import HTMLParser
import urlparse

from lxml.etree import tostring


def str_(value, *args):
    """
    convert data into string
    :rtype: str
    """
    if isinstance(value, str):
        return value

    return value.text


def url_(value, base):
    return urlparse.urljoin(base, value)


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

HTML_PARSER = HTMLParser.HTMLParser()
