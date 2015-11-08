from lxml.etree import _Element

import ciur2
import requests

requests = requests.Session()
response = requests.get("http://example.com")

# print "INFO:", response.content
# rule = ciur.Rule("title", "//h1", [_Element])
# data = ciur.page_html(response.content, rule)
# print type(data)


rule = ciur2.Rule("root", "/html/body", 1,
                  ciur2.Rule("name", ".//h1", [str, 1]), ciur2.Rule("paragrapth", ".//p", [str, 0]))
data = ciur2.page_html(response.content, rule)
print data