import json
from decimal import Decimal

class JsonException(Exception):
    """
    Exception that raise with dictionary explication
    >>> raise JsonException({"key_name1" : "val1", "key_name2" : "val2"})
    Traceback (most recent call last):
        ...
    JsonException: {'key_name2': 'val2', 'key_name1': 'val1'}
    """
    def __init__(self, *args, **kwargs):
        super(JsonException, self).__init__( *args, **kwargs)
        self.value = args[0]


    def __str__(self):
        return repr(self.value)


def str_startswith(text, list_starts):
    """
    >>> str_startswith("banana", ['xr', 'ge', 'bi', 'ba', 'ad'])
    True
    >>> str_startswith("not banana", ['xr', 'ge', 'bi', 'bo', 'ad'])
    False
    """
    for i in list_starts:
        if text.startswith(i):
            return True
    return False


def dt_handler(obj):
    """
    convert all data fields in json intro string format
    """
    if isinstance(obj, Decimal):
        return "Decimal(%s)" %obj

    if isinstance(obj, unicode):
        return obj.encode("utf-8")

    if isinstance(obj, datetime):
        return "Date(%s)" %obj.isoformat()

    if isinstance(obj, ObjectId):
        return "ObjectId('%s')" %str(obj)

    if isinstance(obj, type):
        return str(obj)


def json_dump(obj, sort_keys = False):
    """
    pretty formatting json
    """
    return json.dumps(
        obj,
        sort_keys    = sort_keys,
        indent       = 4,
        default      = dt_handler,
        ensure_ascii = False
    )

