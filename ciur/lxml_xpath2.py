"""
xpath function from xpath2 specification that are not supported native yet in lxml

NOTE:
    local convention for all public xpath2 function is `fn_[a-z]+[a-z0-9_]+` is should begin with "fn_" and
    underscores `_` are converted to dash
    f.e.
        fn_string_join -> string-join(//p)

"""
import re
import sre_constants

from lxml.etree import FunctionNamespace

from ciur.cast import raw_
from ciur.exceptions import CiurBaseException
from ciur.cast import element2text


def fn_replace(context, value, pattern, replacement=""):
    """
    http://www.w3.org/TR/xpath-functions/#func-replace
    :param context: Etree context
    :param replacement:
    :param pattern: regex pattern
    :param value: matches xpath results
    :param context: Etree context
    """
    text = element2text(value)    

    if not text:
        return text

    if not (isinstance(text, basestring) or isinstance(text, list) and len(text) == 1):
        raise CiurBaseException({
            "type": type(text),
            "len": len(text),
            "text": text,
            "context": raw_(context.context_node)
        }, "type checking violation in function `replace`")

    if not isinstance(text, basestring):
        text = text[0]

    try:
        string = re.sub(pattern, replacement, text)
    except (sre_constants.error,) as regex_error:
        raise CiurBaseException("wrong regexp-> %s `%s`" % (str(regex_error), pattern))

    return string


def fn_matches(context, value, regex):
    """
    TODO: add text for this function
    The function returns true if a matches the regular expression supplied as $pattern as influenced by the value
    of $flags, if present; otherwise, it returns false.

    see more http://www.w3.org/TR/xpath-functions/#func-matches

    :param context: DOM context
    :param value: ElementTree or text
    :param regex:
    :return: FIXME return matched node
    """
    if isinstance(value, list):
        return [i for i in [
            fn_matches(context, i_value, regex) for i_value in value
            ] if i is not None]

    text = element2text(value)

    if not text:
        return text

    try:
        match = re.search(regex, text)
    except (sre_constants.error, ) as regexp_error:
        raise CiurBaseException("wrong regexp-> %s `%s`" % (str(regexp_error), regex))

    return value if match else None


def fn_string_join(context, text, separator=""):
    """
    http://www.w3.org/TR/xpath-functions/#func-string-join
    Returns a string created by concatenating the members of the
    text sequence using separator.
    """
    del context
    return separator.join(text)


def fn_upper_case(context, text):
    """
    http://www.w3.org/TR/xpath-functions/#func-upper-case
    :param context:
    :param text:
    :return string
    # TODO add in documentation
    """
    del context
    return text.upper()


def fn_lower_case(context, text):
    """
    http://www.w3.org/TR/xpath-functions/#func-lower-case
    :param context:
    :param text:
    :return string
    # TODO add in documentation
    """
    del context
    return text.lower()

FUNCTION_NAMESPACES = FunctionNamespace(None)

FUNCTION_NAMESPACES.update({k[3:].replace("_", "-"): v for (k, v) in locals().iteritems() if k.startswith("fn_")})
