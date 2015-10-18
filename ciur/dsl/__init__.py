import pyparsing
from pyparsing import lineEnd, empty, FollowedBy
import rfc3987
import StringIO

_input_data = """
url: https://stackoverflow.com/questions/12565098/python-how-to-check-if-a-string-is-a-valid-iri?a=1
name: exam plepage
root = /h3.1 | node # root commenter
    name = .//h1[contains(text(), 'Justin')] | str # text
    count_list = .//h2[contains(text(), 'Andrei')]/p | list | int # lala
    user = .//h5[contains(text(), 'Andrei')]/p | node
        name = ./spam | str
        sure_name = ./bold | str
        age = ./it | int
        hobby = ./li | list | str
        indexes = ./li/bold | list | int
"""

indentStack = [1]

def checkPeerIndent(s,l,t):
    curCol = col(l,s)
    if curCol != indentStack[-1]:
        if (not indentStack) or curCol > indentStack[-1]:
            raise ParseFatalException(s,l,"illegal nesting")
        raise ParseException(s,l,"not a peer entry")

def checkSubIndent(s,l,t):
    curCol = col(l,s)
    if curCol > indentStack[-1]:
        indentStack.append( curCol )
    else:
        raise ParseException(s,l,"not a subentry")

def checkUnindent(s,l,t):
    if l >= len(s): return
    curCol = col(l,s)
    if not(curCol < indentStack[-1] and curCol <= indentStack[-2]):
        raise ParseException(s,l,"not an unindent")

def doUnindent():
    indentStack.pop()

INDENT = lineEnd.suppress() + empty + empty.copy().setParseAction(checkSubIndent)
UNDENT = FollowedBy(empty).setParseAction(checkUnindent)
UNDENT.setParseAction(doUnindent)

def get_bnf():
    """
    get from file:
        results = bnf.parseFile(StringIO.StringIO(input_data), parseAll=True)

    >>> bnf = get_bnf()
    >>> results = bnf.parseString(_input_data, parseAll=True)
    >>> for i in results:
    ...    print i
    [ 'root', '/h3.1 ', ['node'], ' root commenter']
    ['name', ".//h1[contains(text(), 'Justin')] ", ['str'], ' text']
    ['count_list', ".//h2[contains(text(), 'Andrei')]/p ", ['list', 'int'], ' lala']
    ['user', ".//h5[contains(text(), 'Andrei')]/p ", ['node']]
    ['name', './spam ', ['str']]
    ['sure_name', './bold ', ['str']]
    ['age', './it ', ['int']]
    ['hobby', './li ', ['list', 'str']]
    ['indexes', './li/bold ', ['list', 'int']]
    """
    colon = pyparsing.Suppress(":")
    nl = pyparsing.lineEnd.suppress()
    xpath = pyparsing.Word(pyparsing.alphanums + "./[]()_', ")
    key = pyparsing.Word(pyparsing.alphanums + "_")
    pipe = pyparsing.Suppress("|")
    key_url = pyparsing.Literal("url")
    eq = pyparsing.Suppress("=")
    name = pyparsing.Literal("name")
    hash = pyparsing.Suppress("#")

    def parse(url_):
        url_ = url_[0].strip()
        ret = rfc3987.parse(url_, rule='IRI')
        ret["url"] = url_
        return ret

    url = pyparsing.Regex(r".*").leaveWhitespace().setParseAction(parse)

    meta = pyparsing.Group(key_url + colon + url) + pyparsing.Optional(
        pyparsing.Group(name + colon + pyparsing.Word(pyparsing.alphas + " "))
    ) + nl

    comment = pyparsing.Optional(hash + pyparsing.restOfLine)

    type_ = pyparsing.Group(pyparsing.OneOrMore(pipe + pyparsing.oneOf("str int bool node list")))
    rule = key + eq + xpath + type_ + comment

    return pyparsing.Group(meta) + pyparsing.OneOrMore(pyparsing.Group(rule))
