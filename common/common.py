import re
import json
import decimal
import datetime

try:
    from pymongo.objectid import ObjectId
except Exception:
    pass


class JsonException(Exception):
    """
    Exception that raise with dictionary explication
    >>> raise JsonException({"key_name1" : "val1", "key_name2" : "val2"})
    Traceback (most recent call last):
        ...
    JsonException: {'key_name2': 'val2', 'key_name1': 'val1'}
    """
    def __init__(self, *args, **kwargs):
        super(JsonException, self).__init__(*args, **kwargs)
        if args:
            self.value = args[0]


    def __str__(self):
        return repr(self.value)


def str_startswith(text, list_starts):
    """
    Return Matched item else return False
    >>> str_startswith("banana", ['xr', 'ge', 'bi', 'ba', 'ad'])
    'ba'
    >>> str_startswith("not banana", ['xr', 'ge', 'bi', 'bo', 'ad'])
    False
    """
    for i in list_starts:
        if text.startswith(i):
            return i
    return False


def _dt_handler(obj):
    """
    convert all data fields in json intro string format
    """
    if isinstance(obj, re.compile("").__class__):
        return "SRE_Pattern(%s)" %obj.pattern

    if isinstance(obj, decimal.Decimal):
        return "Decimal(%s)" %obj

    if isinstance(obj, unicode):
        return obj.encode("utf-8")

    if isinstance(obj, datetime.datetime):
        return "Date(%s)" %obj.isoformat()

    if isinstance(obj, ObjectId):
        return "ObjectId('%s')" %str(obj)

    if isinstance(obj, type):
        return str(obj)

    return type(obj)


def json_dump(obj, sort_keys=False):
    """
    pretty formatting json
    """
    return json.dumps(
        obj,
        sort_keys=sort_keys,
        indent=4,
        default=_dt_handler,
        ensure_ascii=False
    )

