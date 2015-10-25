from collections import OrderedDict
import warnings
from lxml.etree import _Element
from lxml import etree

import html5lib


def recursive_parse(context_, rule):
    res = context_.xpath(rule.xpath)

    type_list_ = list(rule.type_list)

    for fun, args in type_list_[:-1]:
        tmp = []
        for res_i in res:
            res_i = fun(res_i, *args)

            if res_i not in [None, ""]:
                tmp.append(res_i)
        res = tmp

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
            _ = recursive_parse(res, rule_i)
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
                data = recursive_parse(res_i, rule_i)
                if data:
                    tmp_ordered_dict[rule_i.name] = data

            tmp_list.append(tmp_ordered_dict)

        return tmp_list

    return res


def page_html(doc, rule, warn=None, treebuilder="lxml", namespace=None):
    if warn:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

    context = html5lib.parse(doc, treebuilder=treebuilder, namespaceHTMLElements=namespace)

    ret = recursive_parse(context, rule)
    return ret


def page_xml(doc, rule):
    context = etree.fromstring(doc)

    ret = recursive_parse(context, rule)
    return ret