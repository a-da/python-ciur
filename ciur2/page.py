import warnings

import requests
import html5lib
from lxml import etree

import ciur2

# import requests
#
# s = requests.Session()
# #print s.get("http://example.org").content
# print s.get("file:///etc/debian_version").content

class PageXml(ciur2.CommonEqualityMixin):
    pass


def page_html(doc, rule, warn=None, treebuilder="lxml", namespace=None):
    if warn:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

    context = html5lib.parse(doc, treebuilder=treebuilder, namespaceHTMLElements=namespace)

    def recursive_parse(context_, rule_):
        is_list = False
        for type_i in rule_.type_list:
            if type_i == list:
                is_list = True

        res = context_.xpath(rule_.xpath)

        if not is_list:
            if len(res) > 1:
                assert True, "something bad"
            elif len(res) == 0:
                res = None
            else:
                res = res[0]

        return res

    return recursive_parse(context, rule)








# page = PageHtml()
# dict_ = page.parse("http://example.org")

