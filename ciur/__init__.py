"""
*Ciur is a scrapper layer*
"""
import json
import logging
import warnings
from cookielib import LWPCookieJar
import os

import sys
from requests import Session
from lxml.etree import FunctionNamespace

# noinspection PyProtectedMember
from lxml.etree import _Element as EtreeElement

__title__ = "ciur"
__version__ = "0.1.2"
__author__ = "Andrei Danciuc"
__license__ = "MIT"
__git__ = "https://bitbucket.org/ada/ciur"
__email__ = "python.ciur@gmail.com"

# TODO make configurable
CONF = {
    "IGNORE_WARNING":  False
}


def pretty_json(data):
    """
    wrapper for long code
    :param data: to be converted in json
    :type data: object
    :return: json
    """

    def default(value):
        """
        is a function that should return a serializable version of obj or
        repr(value).

        :param value:
        :type value: object
        :rtype: str
        """
        # noinspection PyProtectedMember
        from lxml.etree import _Comment as EtreeComment

        if isinstance(value, EtreeComment):
            return "<!--%s %s -->" % (value.text, value.tail)

        return repr(value)

    res = json.dumps(data, indent=4, ensure_ascii=False, default=default)
    return res.encode("utf-8") if isinstance(res, unicode) else res


class CommonEqualityMixin(object):  # pylint: disable=too-few-public-methods
    """
    boilerplate class for equal method
    """
    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
            self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


def get_session(callback_log_in, cookie_file_path):
    """
    get session with cookies file support save / load

    :param cookie_file_path:
        :type cookie_file_path: str
    :param callback_log_in:
        :type callback_log_in: function

    :rtype: Session
    """

    session = Session()

    session.cookies = LWPCookieJar(cookie_file_path)

    if not os.path.exists(cookie_file_path):
        print "[INFO] setting cookies"
        session.cookies.save()
        callback_log_in(session)
    else:
        print "[INFO] loading cookies"
        session.cookies.load(ignore_discard=True)

    return session


def load_xpath_functions(locals_):
    """
    load xpath functions into lxml scopes
    see http://lxml.de/extensions.html#the-functionnamespace

    :param locals_:  dictionary containing the current scope's local variables.
        :type locals_: dict
    """
    locals()
    function_namespaces = FunctionNamespace(None)

    function_namespaces.update({
        k[3:].replace("_", "-"): v for (k, v) in locals_.iteritems()
        if k.startswith("fn_")
    })


def element2text(value):
    """
    convert value to text if is EtreeElement or strip value is is text already
    :param value:
        :type value: EtreeElement or list or str
    :rtype str or iterable[str]
    """
    if isinstance(value, EtreeElement):
        return value.text
    elif isinstance(value, list) and len(value) > 0:
        return [element2text(i) for i in value]

    if not value:
        return value

    return value.strip()


def path(relative, root=__file__):
    """
    :param relative: path
        :type relative: str
    :param root: path
        :type root: str
    :return: absolute path
    :rtype: str
    """
    root_ = os.path.dirname(os.path.abspath(root))
    return os.path.join(root_, relative)


def open_file(relative, root=__file__, mode='r'):
    """
    :param relative: path
        :type relative: str
    :param root: path
        :type root: str
    :param mode: file mode read, write, binary ...
        :type mode: str
    :return: absolute path
    :rtype: FileIO
    """
    return open(path(relative, root), mode)


def get_logger(name, formatter=None, handler=None, level=logging.INFO):
    """
    
    :param name: 
    :param formatter: 
    :param handler: 
    :param level: 
    :return: logger
        :rtype: logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = handler or logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(
        formatter or
        "%(asctime)s [%(levelname)s] %(funcName)s(%(lineno)d) - %(message)s"
    ))
    logger.addHandler(handler)

    def custom_warn(message, category, filename, lineno, *_):
        logger.warn(
            warnings.formatwarning(message, category, filename, lineno).strip()
        )

    warnings.showwarning = custom_warn

    return logger

