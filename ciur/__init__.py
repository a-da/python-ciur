"""
*Ciur is a scrapper layer*
"""
import json

# noinspection PyProtectedMember
from lxml.etree import _Comment as EtreeComment

__title__ = "ciur"
__version__ = "0.1"
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
        is a function that should return a serializable version of obj or repr(value).

        :param value:
        :type value: object
        :rtype: str
        """
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
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)
