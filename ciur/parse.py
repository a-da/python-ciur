"""
parse page based on ciur rules and page type (xml, html ...)
"""

from collections import OrderedDict
import warnings

# noinspection PyProtectedMember
from lxml.etree import _Element

from lxml import etree
import html5lib

from ciur import CiurException

NOT_NULL_TYPES = (bool, float, basestring)


def _recursive_parse(context_, rule, namespace=None, url=None):
    """
    recursive parse embedded rules
    """
    try:
        res = context_.xpath(rule.xpath, namespaces=namespace)
    except etree.XPathEvalError, e:
        raise CiurException(e, {"rule.name": rule.name, "rule.xpath": rule.xpath})

    if isinstance(res, NOT_NULL_TYPES):
        res = [res]

    # ignore size match check to use it later
    for fun, args in rule.type_list[:-1]:
        tmp = []
        for res_i in res:
            if fun.__name__ == "url_":
                res_i = fun(res_i, url)
            else:
                res_i = fun(res_i, *args)

            # filter null results
            if res_i not in [None, ""]:
                tmp.append(res_i)
        res = tmp

    if isinstance(res, _Element):
        ordered_dict = OrderedDict()
        for rule_i in rule.rule[:]:
            _ = _recursive_parse(res, rule_i, url=url, namespace=namespace)

            if _ or _ is False:
                ordered_dict[rule_i.name + "x"] = _

        res = {
            rule.name: ordered_dict
        }

    elif isinstance(res, list) and len(res) and isinstance(res[0], _Element):
        tmp_list = []
        for res_i in res:
            tmp_ordered_dict = OrderedDict()
            for rule_i in rule.rule:
                data = _recursive_parse(res_i, rule_i, url=url, namespace=namespace)
                if data:
                    tmp_ordered_dict.update(data)

            if tmp_ordered_dict:
                tmp_list.append(tmp_ordered_dict)

        res = tmp_list

    # do size match check
    size, args = rule.type_list[-1]
    try:
        size(len(res), *args)
    except Exception, e:
        raise Exception("[ERROR] %s, on rule `%s` %s but got %s element" % (e.message, rule.name, args, len(res)))

    if not rule.name.endswith("_list") and len(res) == 1:
        res = res[0]

    if rule.rule and isinstance(res, NOT_NULL_TYPES):
        import sys
        sys.stderr.write("[WARN] there are children that were ignored on rule.name=`%s`\n" % rule.name)

    if not res and not isinstance(res, NOT_NULL_TYPES):
        return res
    else:
        if res == "":
            return None

        if ":" not in rule.name:
            return {rule.name: res}

        rule_name_list = rule.name.split(":")
        if rule_name_list[-1].endswith("_list"):
            rule_name_list = [i if i.endswith("_list") else i + "_list" for i in rule_name_list]

        return OrderedDict((i, res) for i in rule_name_list)


def html(doc, rule, warn=None, treebuilder="lxml", namespace=None, url=None):
    """
    use this function if page is html
    """
    if warn:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

    context = html5lib.parse(doc, treebuilder=treebuilder, namespaceHTMLElements=namespace)

    ret = _recursive_parse(context, rule, url=url, namespace=namespace)
    return ret


def xml(doc, rule, namespace=None, url=None):
    """
    use this function if page is xml
    """
    context = etree.fromstring(doc)

    ret = _recursive_parse(context, rule, url=url, namespace=namespace)
    return ret
