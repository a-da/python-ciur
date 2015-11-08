import requests

from ciur import bnf_parser, parse, pretty_json
from ciur.rule import Rule


requests = requests.Session()
response = requests.get("https://999.md/ro/list/household-appliances/hoods?page=2")
# print response.content

res = bnf_parser.to_dict(open("999.md.ciur").read())
rule = Rule.from_dict(res)
data = parse.html(response.content, rule)
print pretty_json(data)
