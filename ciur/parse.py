"""
parse page based on ciur rules and page type (xml, html ...)
"""

from collections import OrderedDict
import warnings

# noinspection PyProtectedMember
from lxml.etree import _Element

from lxml import etree
import html5lib


def _recursive_parse(context_, rule, url=None):
    """
    recursive parse embedded rules
    """
    res = context_.xpath(rule.xpath)

    type_list_ = rule.type_list

    # ignore size match check to use it later
    for fun, args in type_list_[:-1]:
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

    # do size match check
    size, args = type_list_[-1]
    try:
        size(len(res), *args)
    except Exception, e:
        raise Exception("[ERROR] %s, %s %s, but got %s" % (e.message, rule.name, args, len(res)))

    if len(res) == 1:
        res = res[0]

    if isinstance(res, _Element):
        ordered_dict = OrderedDict()
        for rule_i in rule.rule[:]:
            _ = _recursive_parse(res, rule_i, url)
            if _:
                ordered_dict[rule_i.name] = _

        return {
            rule.name: ordered_dict
        }
    elif isinstance(res, list) and len(res) and isinstance(res[0], _Element):
        tmp_list = []
        for res_i in res:
            tmp_ordered_dict = OrderedDict()
            for rule_i in rule.rule:
                data = _recursive_parse(res_i, rule_i, url)
                if data:
                    tmp_ordered_dict[rule_i.name] = data

            tmp_list.append(tmp_ordered_dict)

        return tmp_list

    return res


def html(doc, rule, warn=None, treebuilder="lxml", namespace=None, url=None):
    """
    use this function if page is html
    """
    if warn:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

    context = html5lib.parse(doc, treebuilder=treebuilder, namespaceHTMLElements=namespace)

    ret = _recursive_parse(context, rule, url=url)
    return ret


def xml(doc, rule):
    """
    use this function if page is xml
    """
    context = etree.fromstring(doc)

    ret = _recursive_parse(context, rule)
    return ret