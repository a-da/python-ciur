import warnings
from lxml.etree import _Element

import html5lib


def size(got, expect):
    assert got == expect, "expect size `%s`, got `%s`" % (expect, got)


def ceva(value, *args):
    return value


def _str(value):
    return value.text


def recursive_parse(context_, rule):
    res = context_.xpath(rule.xpath)

    type_list_ = list(rule.type_list)

    _size = 0
    if isinstance(type_list_[-1], int):
        _size = type_list_.pop()

    for type_i in type_list_:
        tmp = []
        for res_i in res:
            if type_i is str:
                fun = _str
            else:
                fun = ceva

            res_i = fun(res_i)

            if res_i is not None:
                tmp.append(res_i)
        res = tmp

    if _size:  # check if for expected size
        size(len(res), _size)

        if _size == 1:
            res = res[0]

    if isinstance(res, _Element):
        tmp = {}
        for rule_i in rule.rule[:]:
            _ = recursive_parse(res, rule_i)
            tmp[rule_i.name] = _

        return {
            rule.name: tmp
        }

    return res


def page_html(doc, rule, warn=None, treebuilder="lxml", namespace=None):
    if warn:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

    context = html5lib.parse(doc, treebuilder=treebuilder, namespaceHTMLElements=namespace)

    return recursive_parse(context, rule)








# page = PageHtml()
# dict_ = page.parse("http://example.org")

