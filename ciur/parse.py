"""
parse page based on ciur rules and page type (xml, html ...)

NOTE:
    local convention for all public paring function is `[a-z]+[a-z0-9_]+_type`
    is should end with "_type"
"""
import StringIO
from collections import OrderedDict

# noinspection PyProtectedMember
from lxml.etree import _Element as EtreeElement

from lxml.cssselect import CSSSelector
from lxml import etree

from pdfminer.pdfdevice import TagExtractor
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from ciur.exceptions import CiurBaseException
from ciur.models import Document

NOT_NULL_TYPES = (bool, float, basestring)
_DATA_TYPE_DICT = "_dict"


def _is_list(value):
    """
    check if is list
    :param value:
    :type value: str
    :rtype bool
    """
    return value.endswith("_list")


def _is_dict(value):
    """
    check if is dict
    :param value:
    :type value: str
    :rtype bool
    """
    return value.endswith("_dict")


def _type_list_casting(type_list, res, url):
    for fun, args in type_list[:-1]:
        tmp = []
        for res_i in res:
            if fun.__name__.startswith("fn_"):
                res_i = fun(None, res_i, *args)
            elif fun.__name__ == "url_":
                res_i = fun(res_i, url)
            else:
                try:
                    res_i = fun(res_i, *args)
                except TypeError, type_error:
                    print type_error
                    # TODO fix this

            # filter null results
            if res_i not in [None, ""]:
                tmp.append(res_i)

        res = tmp

    return res


def _get_xpath(selector, selector_type):
    xpath = selector.decode("utf-8") if isinstance(selector, str) else selector
    if selector_type == "css":
        sel = CSSSelector(xpath)
        xpath = sel.path

    return xpath


def _shrink(res, it_list):
    if not it_list and isinstance(res, list) and len(res) == 1:
        return _shrink(res[0], it_list)

    return res


def _stretch(res):
    if isinstance(res, NOT_NULL_TYPES):
        res = [res]

    return res


def _name_colon(res, name):
    rule_name_list = name.split(":")
    if _is_list(rule_name_list[-1]):
        rule_name_list = [
            i if _is_list(i) else i + "_list" for i in rule_name_list
        ]

    return OrderedDict((i, res) for i in rule_name_list)


def _size_match_assert(res, rule, url, size, args):
    # do size match check
    try:
        size(len(res), *args)
    except (AssertionError,) as assert_error:
        raise CiurBaseException({
            "rule.name": rule.name,
            "rule.selector": rule.selector,
            "url": url
        }, "size-match error -> %s, on rule `%s` %s but got %s element" % (
            assert_error.message, rule.name, args, len(res)
        ))


def _recursive_parse(context_, rule, namespace=None, url=None):
    """
    recursive parse embedded rules
    """

    xpath = _get_xpath(rule.selector, rule.selector_type)
    try:
        res = context_.xpath(xpath, namespaces=namespace)
    except (etree.XPathEvalError,) as xpath_eval_error:
        raise CiurBaseException(xpath_eval_error, {
            "rule.name": rule.name, "rule.selector": rule.selector
        })

    res = _stretch(res)
    res = _type_list_casting(rule.type_list, res, url)

    if isinstance(res, list) and len(res) and isinstance(res[0], EtreeElement):
        tmp_list = []
        for res_i in res:
            tmp_ordered_dict = OrderedDict()
            for rule_i in rule.rule:
                data = _recursive_parse(
                    res_i, rule_i, url=url, namespace=namespace
                )
                if data:
                    tmp_ordered_dict.update(data)

            if tmp_ordered_dict:
                tmp_list.append(tmp_ordered_dict)

        res = tmp_list

    # filter empty items
    res = [i for i in res if i != ""]

    res = _stretch(res)

    if _is_dict(rule.name):

        # pylint: disable=redefined-variable-type
        res = OrderedDict((i.pop(rule.rule[0].name), i) for i in res)

    _size_match_assert(res, rule, url, *rule.type_list[-1])

    res = _shrink(res, _is_list(rule.name))

    if rule.rule and (
            isinstance(res, NOT_NULL_TYPES) or
            res and isinstance(res, list) and
            isinstance(res[0], NOT_NULL_TYPES)
    ):
        import sys
        sys.stderr.write("[WARN] there are children that were ignored on"
                         " rule.name=`%s`\n" % rule.name)

    if not res and not isinstance(res, NOT_NULL_TYPES):
        return res
    else:
        if res == "":
            return None

        if ":" not in rule.name:
            return {rule.name: res}

        return _name_colon(res, rule.name)


def html_type(document, rule):
    """
    use this function if page is html
    :param tree_builder: collection of modules names for building different
        kinds of tree from HTML documents.
        :type tree_builder: str

    :param rule:
        :type rule: Rule

    :param document: Document to be parsed
        :type document: Document

    :rtype: OrderedDict
    """    
    
    import html5lib
    # context = html5parser.document_fromstring(document.content)
    context = html5lib.parse(
         document.content,
         treebuilder="lxml",
         namespaceHTMLElements=document.namespace,
         encoding=document.encoding
    )

    ret = _recursive_parse(
        context,
        rule,
        url=document.url,
        namespace={'html': 'http://www.w3.org/1999/xhtml'} # document.namespace
    )
    return ret


def xml_type(document, rule):
    """
    use this function if page is xml
    :param rule:
        :type rule: Rule

    :param document: Document to be parsed
        :type document: Document

    :rtype: OrderedDict
    """

    context = etree.fromstring(document.content)    

    ret = _recursive_parse(
        context,
        rule,
        url=document.url,
        namespace=document.namespace
    )
    return ret


def pdf_type(document, rule):
    """
    use this function if page is pdf
    TODO: do not forget to document this
    :param rule:
        :type rule: Rule

    :param document: Document to be parsed
        :type document: Document

    :rtype: OrderedDict
    """

    resource_manager = PDFResourceManager(caching=True)

    out_fp = StringIO.StringIO()
    in_fp = StringIO.StringIO(document.content)

    device = TagExtractor(resource_manager, out_fp, codec='utf-8')

    interpreter = PDFPageInterpreter(resource_manager, device)
    for page in PDFPage.get_pages(in_fp):
        page.rotate %= 360
        interpreter.process_page(page)

    out_fp.seek(0)  # reset the buffer position to the beginning
    
    xml = Document(
        out_fp.read(),
        namespace=document.namespace,
        url=document.url
    )
    return xml_type(xml, rule)
