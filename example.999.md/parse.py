import requests


from ciur import bnf_parser, parse, pretty_json
from ciur.rule import Rule

requests = requests.Session()
#print response.content

res = bnf_parser.to_dict(open("999.md.ciur").read())
rule = Rule.from_list(res)

import time
for i in range(500, 1000):
    print i
    response = requests.get("https://999.md/ro/list/household-appliances/hoods?page=%d" % i)
    #print rule
    data = parse.html(response.content, rule[0])
    open("%d.json" % i, "w").write(pretty_json(data))
    time.sleep(0.5)



from pyparsing import *
# # .ignore(cStyleComment)
# cFunction = Word(alphas) + Optional(cStyleComment) + "(" + Group(Optional(delimitedList(Word(nums)|Word(alphas)))) + ")"
# #cFunction
#
# s = "abc/*d*/ (1, 2, def, 5)"
# print cFunction.parseString(s, parseAll=True)


# identifier = Word(alphas, alphanums + "_")  # <url> ./url str +1 => label of rule
# xpath = Suppress("`") + Word(alphas+"./", printables + " ", excludeChars="`") + Suppress("`")  # url <./url> str +1 => xpath query
#
# type_list = Group(
#     Optional(Literal("str") | Literal("int")) +  # url ./url <str> +1 => functions chains for transformation
#     Regex("[\+*]\d*")   # url ./url str <+1>  => size match: + mandatory, * optional, \d+ exact len
# )
#
# rule = identifier + xpath + type_list  # <url ./url str +1> => rule line
# rule.ignore(pythonStyleComment)
# s = \
# "title `.//div[@class='ads-list-photo-item-title ']//a` str *"
#
# print rule.parseString(s)
