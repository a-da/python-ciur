import pyparsing
import rfc3987

input_data = """
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


def get_bnf():
    colon = pyparsing.Suppress(":")
    nl = pyparsing.lineEnd.suppress()
    xpath = pyparsing.Word(pyparsing.alphanums + "./[]()_', ")
    key = pyparsing.Word(pyparsing.alphanums + "_")
    pipe = pyparsing.Suppress("|")
    key_url = pyparsing.Literal("url")
    eq = pyparsing.Suppress("=")
    name = pyparsing.Literal("name")
    hash = pyparsing.Suppress("#")

    url = pyparsing.Regex(r".*").leaveWhitespace().setParseAction(lambda x: rfc3987.parse(x[0].strip(), rule='IRI'))

    meta = pyparsing.Group(key_url + colon + url) + \
            pyparsing.Optional(pyparsing.Group(name + colon + pyparsing.Word(pyparsing.alphas + " "))) + nl

    comment = pyparsing.Optional(hash + pyparsing.restOfLine)

    type_ = pyparsing.Group(pyparsing.OneOrMore(pipe + pyparsing.oneOf("str int bool node list")))
    rule = key + eq + xpath + type_ + comment

    return pyparsing.Group(meta) + pyparsing.OneOrMore(pyparsing.Group(rule))


if __name__ == "__main__":
    bnf = get_bnf()
    results = bnf.parseString(input_data, parseAll=True)
    for i in results:
        print i

    import StringIO

    results = bnf.parseFile(StringIO.StringIO(input_data), parseAll=True)
    for i in results:
        # print i
        pass
