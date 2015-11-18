"""
xpath function from xpath2 specification that are not supported native yet in lxml
"""
import re
import sre_constants

from lxml.etree import FunctionNamespace

from cast import raw_
from ciur import CiurException
from ciur.cast import element2text


def fn_replace(context, value, pattern, replacement):
    """
    http://www.w3.org/TR/xpath-functions/#func-replace

    Examples:

        replace("abracadabra", "bra", "*") returns "a*cada*"

        replace("abracadabra", "a.*a", "*") returns "*"

        replace("abracadabra", "a.*?a", "*") returns "*c*bra"

        replace("abracadabra", "a", "") returns "brcdbr"

        replace("abracadabra", "a(.)", "a$1$1") returns "abbraccaddabbra"

        replace("abracadabra", ".*?", "$1") raises an error, because the pattern matches the zero-length string

        replace("AAAA", "A+", "b") returns "b"

        replace("AAAA", "A+?", "b") returns "bbbb"

        replace("darted", "^(.*?)d(.*)$", "$1c$2") returns "carted". The first d is replaced.

    """
    text = element2text(value)

    if not text:
        return text

    if not (isinstance(text, list) and len(text) == 1):
        raise CiurException({
            "type": type(text),
            "len": len(text),
            "text": text,
            "context": raw_(context.context_node)
        }, "type checking violation in function `matches`")

    try:
        string = re.sub(pattern, replacement, text[0])
    except sre_constants.error, e:
        raise CiurException("wrong regexp-> %s `%s`" % (str(e), pattern))

    return string


def fn_matches(context, value, regex):
    """
    The function returns true if a matches the regular expression supplied as $pattern as influenced by the value
    of $flags, if present; otherwise, it returns false.

    see more http://www.w3.org/TR/xpath-functions/#func-matches

    :param context: DOM context
    :param text: input as string
    :param regex:
    :return:
    """
    text = element2text(value)

    if not text:
        return text

    if not (isinstance(text, list) and len(text) == 1):
        raise CiurException({
            "type": type(text),
            "len": len(text),
            "text": text,
            "context": raw_(context.context_node)
        }, "type checking violation in function `matches`")

    try:
        m = re.search(regex, text[0])
    except sre_constants.error, e:
        raise CiurException("wrong regexp-> %s `%s`" % (str(e), regex))

    return bool(m)


def fn_string_join(context, text, separator=""):
    """
    http://www.w3.org/TR/xpath-functions/#func-string-join
    Returns a string created by concatenating the members of the
    text sequence using separator.
    """
    return separator.join(text)


ns = FunctionNamespace(None)


ns.update({k[3:].replace("_", "-"): v for (k, v) in locals().iteritems() if k.startswith("fn_")})






