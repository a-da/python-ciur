"""
*Ciur is a scrapper layer*
"""
import json
import logging
import os
import sys
import warnings

# noinspection PyProtectedMember

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
    :param name: usually __name__
        :type name: str
    :param formatter: Formatter instances are used to convert a
        LogRecord to text.
        :type formatter: logging.Formatter
    :param handler: Handler instances dispatch logging events to
        specific destinations.
        :type handler: logging.Handler
    :param level: log level
        :type level: long or int
    :return: logger
        :rtype: logging.Logger
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
        """
        redirect logs from warning module to log module
        :param message:
            :type message: str
        :param category: a class that the warning must be a subclass of
            :type category: warnings.WarningMessage
        :param filename:
            :type filename: str
        :param lineno:
            :type lineno: int
        :param _: unused
        """
        logger.warn(
            warnings.formatwarning(message, category, filename, lineno).strip()
        )

    warnings.showwarning = custom_warn

    return logger

