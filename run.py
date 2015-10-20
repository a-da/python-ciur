from lxml.etree import _Element

import ciur2
import requests

requests = requests.Session()
response = requests.get("http://example.com")

# print "INFO:", response.content
# rule = ciur2.Rule("title", "//h1", [_Element])
# data = ciur2.page_html(response.content, rule)
# print type(data)


rule = ciur2.Rule("root", "/html/body", [_Element], ciur2.Rule("name", ".//h1", [_Element]), ciur2.Rule("paragrapth", ".//p", [_Element]))
data = ciur2.page_html(response.content, rule)
print type(data)