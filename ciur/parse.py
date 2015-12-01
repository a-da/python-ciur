"""
parse page based on ciur rules and page type (xml, html ...)

NOTE:
    local convention for all public paring function is `[a-z]+[a-z0-9_]+_type` is should end with "_type"
"""
import StringIO
from collections import OrderedDict
import warnings

# noinspection PyProtectedMember
from lxml.etree import _Element as EtreeElement

from lxml import etree
import html5lib
from pdfminer.pdfdevice import TagExtractor
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from ciur import CiurException

NOT_NULL_TYPES = (bool, float, basestring)
_DATA_TYPE_DICT = "_dict"


def _is_list(value):
    return value.endswith("_list")


def _is_dict(value):
    return value.endswith("_dict")


def _recursive_parse(context_, rule, namespace=None, url=None):
    """
    recursive parse embedded rules
    """
    xpath = rule.selector.decode("utf-8") if isinstance(rule.selector, str) else rule.selector
    if rule.selector_type == "css":
        from lxml.cssselect import CSSSelector
        sel = CSSSelector(xpath)
        xpath = sel.path
    try:
        res = context_.xpath(xpath, namespaces=namespace)
    except etree.XPathEvalError, e:
        raise CiurException(e, {"rule.name": rule.name, "rule.selector": rule.selector})

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

    if isinstance(res, EtreeElement):
        ordered_dict = OrderedDict()
        for rule_i in rule.rule:
            data = _recursive_parse(res, rule_i, url=url, namespace=namespace)

            if data or data is False:
                ordered_dict[rule_i.name + "x"] = data

        res = {
            rule.name: ordered_dict
        }

    elif isinstance(res, list) and len(res) and isinstance(res[0], EtreeElement):
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

    # filter empty items
    res = [i for i in res if i != ""]
    if isinstance(res, NOT_NULL_TYPES):
        res = [res]

    # do size match check
    size, args = rule.type_list[-1]
    try:
        size(len(res), *args)
    except Exception, e:
        raise CiurException({
            "rule.name": rule.name,
            "rule.selector": rule.selector,
            "url": url
        }, "size-match error -> %s, on rule `%s` %s but got %s element" % (e.message, rule.name, args, len(res)))

    if not _is_list(rule.name) and isinstance(res, list) and len(res) == 1:
        res = res[0]
        if isinstance(res, list) and len(res) == 1:  # list in list use case
            res = res[0]
    elif _is_dict(rule.name) and isinstance(res, list):
        res = OrderedDict((i.popitem(last=False)[1], i) for i in res)

    if rule.rule and (
                isinstance(res, NOT_NULL_TYPES) or
                res and isinstance(res, list) and isinstance(res[0], NOT_NULL_TYPES)
    ):
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
        if _is_list(rule_name_list[-1]):
            rule_name_list = [i if _is_list(i) else i + "_list" for i in rule_name_list]

        return OrderedDict((i, res) for i in rule_name_list)


def html_type(doc, rule, warn=None, treebuilder="lxml", namespace=None, url=None, encoding=None):
    """
    use this function if page is html
    """
    if warn:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

    context = html5lib.parse(doc, treebuilder=treebuilder, namespaceHTMLElements=namespace, encoding=encoding)

    ret = _recursive_parse(context, rule, url=url, namespace=namespace)
    return ret


def xml_type(doc, rule, namespace=None, url=None, encoding=None):
    """
    use this function if page is xml
    """
    context = etree.fromstring(doc)

    ret = _recursive_parse(context, rule, url=url, namespace=namespace)
    return ret


def pdf_type(doc, rule, namespace=None, url=None, encoding=None):
    """
    use this function if page is pdf
    TODO: do not forget to document this
    """

    resource_manager = PDFResourceManager(caching=True)

    out_fp = StringIO.StringIO()  # TODO: check if is close correctly
    in_fp = StringIO.StringIO(doc)

    device = TagExtractor(resource_manager, out_fp, codec='utf-8')

    interpreter = PDFPageInterpreter(resource_manager, device)
    for page in PDFPage.get_pages(in_fp):
        page.rotate %= 360
        interpreter.process_page(page)

    out_fp.seek(0)  # reset the buffer position to the beginning

    return xml_type(out_fp.read(), rule, namespace=namespace, url=url)
