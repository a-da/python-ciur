"""
*Ciur is a scrapper layer*
"""
import json


def pretty_json(dict_):
    return json.dumps(dict_, indent=4, ensure_ascii=False).encode("utf-8")


class CommonEqualityMixin(object):
    """
    boilerplate class for equal method
    """
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)