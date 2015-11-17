"""
*Ciur is a scrapper layer*
"""
import json


def pretty_json(dict_):
    """
    wrapper for long code
    """
    return json.dumps(dict_, indent=4, ensure_ascii=False, default=lambda x: repr(x)).encode("utf-8")


class CiurException(BaseException):
    """
    exception class used in ciur
    """
    def __init__(self, data, *args, **kwargs):
        BaseException.__init__(self, *args, **kwargs)
        self._data = data

    def __str__(self):
        return "%s, %s" %(BaseException.__str__(self), self._data)


class CommonEqualityMixin(object):
    """
    boilerplate class for equal method
    """
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)
