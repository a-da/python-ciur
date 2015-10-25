import json

from common_equality_mixin import CommonEqualityMixin
from page import page_html, page_xml
from rule import Rule


def pretty_json(dict_):
    return json.dumps(dict_, indent=4, ensure_ascii=False).encode("utf-8")





