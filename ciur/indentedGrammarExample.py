# indentedGrammarExample.py
#
# Copyright (c) 2006, Paul McGuire
#
# A sample of a pyparsing grammar using indentation for 
# grouping (like Python does).
#
import pyparsing
from pyparsing import *

data = """\
root /jobs/job +
    title ./title str +
    url ./url str +1
    location . *
        country ./country str +1
        city ./city str +1
        zip ./postalcode str *1
        efe
"""

indentStack = [1]


def check_peer_indent(s, l, t):
    cur_col = col(l, s)
    if cur_col != indentStack[-1]:
        if (not indentStack) or cur_col > indentStack[-1]:
            raise ParseFatalException(s, l, "illegal nesting")
        raise ParseException(s, l, "not a peer entry")


def check_sub_indent(s, l, t):
    cur_col = col(l, s)
    if cur_col > indentStack[-1]:
        indentStack.append(cur_col)
    else:
        raise ParseException(s, l, "not a subentry")


def check_unindent(s, l, t):
    if l >= len(s):
        return

    _cur_col = col(l, s)
    if not(_cur_col < indentStack[-1] and _cur_col <= indentStack[-2]):
        raise ParseException(s, l, "not an unindent")


def do_unindent():
    indentStack.pop()
    
INDENT = lineEnd.suppress() + empty + empty.copy().setParseAction(check_sub_indent)
UNDENT = FollowedBy(empty).setParseAction(check_unindent).setParseAction(do_unindent)


identifier = Word(alphas, alphanums)
xpath = Regex("\.?(/\w+)*")
type_list = Optional(Literal("str") | Literal("int")) + Regex("[+*]\d*")  # oneOf("str int +")
line = identifier + xpath + Group(ZeroOrMore(type_list))

stmt = Forward()
suite = OneOrMore(stmt.setParseAction(check_peer_indent))

funcDef = Group(line + Optional(INDENT + suite + UNDENT))

stmt << funcDef


def uuu(in_):
    """
    :rtype: ParseResults
    """
    parseTree_ = suite.parseString(in_
                                   , parseAll=True
                                   )
    return parseTree_

#print (data)
#parseTree = suite.parseString(data, parseAll=True)
parseTree = uuu(data)
#print(suite)
import pprint


pprint.pprint( parseTree.asList() )

