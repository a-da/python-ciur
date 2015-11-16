"""
xpath function from xpath2 specification that are not supported native yet in lxml
"""
import sre_constants

from lxml.etree import FunctionNamespace

from ciur import CiurException


def matches(context, text, regex):
    """
    The function returns true if a matches the regular expression supplied as $pattern as influenced by the value
    of $flags, if present; otherwise, it returns false.

    see more http://www.w3.org/TR/xpath-functions/#func-matches

    :param context: DOM context
    :param text: input as string
    :param regex:
    :return:
    """
    if not text:
        return text

    assert isinstance(text, list) and len(text) == 1

    import re
    try:
        m = re.search(regex, text[0])
    except sre_constants.error, e:
        raise CiurException("wrong regexp-> %s `%s`" % (str(e), regex))

    return bool(m)


def string_join(context, text, separator=""):
    """
    http://www.w3.org/TR/xpath-functions/#func-string-join
    Returns a string created by concatenating the members of the
    text sequence using separator.
    """
    return separator.join(text)


ns = FunctionNamespace(None)


ns.update({
    'matches': matches,
    'string-join': string_join
})



