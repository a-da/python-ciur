from collections import OrderedDict
from ciur.dsl import get_bnf

test_res = [
    [['url', {'fragment': None, 'authority': 'stackoverflow.com', 'url': 'https://stackoverflow.com/questions/12565098/python-how-to-check-if-a-string-is-a-valid-iri?a=1', 'query': 'a=1', 'path': '/questions/12565098/python-how-to-check-if-a-string-is-a-valid-iri', 'scheme': 'https'}], ['name', 'exam plepage']],
    ['root', '/h3.1', ['node'], ' root commenter', [
        ['name', ".//h1[contains(text(), 'Justin')]", ['str'], ' text'],
        ['count_list', ".//h2[contains(text(), 'Andrei')]/p", ['list', 'int'], ' lala'],
        ['user', ".//h5[contains(text(), 'Andrei')]/p", ['node'], [
            ['name', './spam', ['str']],
            ['sure_name', './bold', ['str']],
            ['age', './it', ['int']],
            ['hobby', './li', ['list', 'str']],
            ['indexes', './li/bold', ['list', 'int']]
            ]
         ]
    ]
    ]
]


# class Node(object):
#     def __init__(self, xpath):
#         if xpath == "/h3.1":
#             return Node()
#         if xpath == ".//h1[contains(text(), 'Justin')]":
#             return "some text"



class Ciur2(object):
    _lxml = "lxml"

    def __init__(self, file_):
        #bnf = get_bnf()
        #res = bnf.parseFile(file_, parseAll=True)
        res = test_res
        self._meta_url = res[0][0][1]
        self._meta_name = res[0][1][1]
        self._rules = res[1]

    # def run(self):
    #     print self._rules[1]
    #     # noinspection PyTypeChecker
    #     page_context = Node("/")
    #
    #     self._parse(page_context, self._rule, None)

        # for rule_i in self._rules:
        #     print rule_i
        #     name = rule_i[0]
        #     xpath = rule_i[1]
        #     type_list = rule_i[2]
        #     if len(rule_i) == 4:
        #         comment = rule_i[3]
        #
        #     context = self._extract(self._root_context, xpath, name)
        #     data = self._validate_type(type_list, context)
        #     if isinstance(data, Node):
        #         #self._parse(data, self._rules[1:], rule)
        #         print "parse1"
        #     else:
        #         print "done1"

    # def _parse_page(self, xpath):
    #     return Node(xpath) if self._lxml else None
    #
    # @classmethod
    # def _validate_type(cls, type_list, context):
    #     return context if type_list else None
    #
    # def _parse(self, context, rules, prev_rule=None):
    #     name = rules[0]
    #     xpath = rules[1]
    #     type_list = rules[2]
    #     next_rule = rules[3] if isinstance(rules[3], list) else rules[4]
    #
    #     data = self._validate_type(type_list, context)
    #
    #     if isinstance(data, Node):
    #         self._parse(data, self._rules[1:], rule)
    #     else:
    #         print "done2"

    # def _extract(self, context, xpath, name=None):
    #     if name in "root":
    #         return Node(xpath)
    #
    #     if name in "name":
    #         return "str"
    #
    #     if name in "user":
    #         return Node(xpath)


class Page(object):
    def __init__(self, url):
        pass

    def xpath(self, xpath):
        if xpath == "/h3.1":
            return self

        if xpath in [".//h1[contains(text(), 'Justin')]", './spam', './bold']:
            return "some text"

        if xpath in [".//h2[contains(text(), 'Andrei')]/p", './li/bold']:
            return [1, 2, 3, 4, 5]

        if xpath == "./it":
            return 666

        if xpath == "./li":
            return ["a", "b", "c"]

        if xpath == ".//h5[contains(text(), 'Andrei')]/p":
            return self

        if xpath == "'./spam'":
            return self

        print "++++++++++++++++", xpath
        return "other"


def validate(type_list, data):
    def type_1(data):
        return data

    def type_2(data):
        return data

    def node(data):
        return data

    def str_(data):
        return data

    def list_(data):
        return data

    def int_(data):
        return data

    m = {
        "type_1": type_1,
        "type_2": type_2,
        "node": node,
        "str": str_,
        "list": list_,
        "int": int_,
    }

    for type_i in type_list:
        data = m[type_i](data)

    return data


class Ciur3(object):

    def __init__(self, file_):
        #bnf = get_bnf()
        #res = bnf.parseFile(file_, parseAll=True)
        res = test_res
        self._meta_url = res[0][0][1]
        self._meta_name = res[0][1][1]
        self._rules = res[1]

    def parse(self, url, rule=None, context=None, comment=None):
        if not rule:
            rule = self._rules
            context = Page(url)

        name = rule[0]
        xpath = rule[1]
        type_list = rule[2]

        print "[INOF]", name, xpath, type_list, comment

        if len(rule) == 3:  # done have no comment or child
            child = None
        else:
            if isinstance(rule[3], str):  # have comment only
                comment = rule[3]
                if len(rule) == 5:
                    child = rule[4]
                else:
                    child = None
            else:  # have nor comment but have child
                child = rule[3]



        context = context.xpath(xpath)
        data = validate(type_list, context)

        if child:
            child_dict = OrderedDict()
            print "[INFO] process child"
            for child_i in child:
                res = self.parse(url, rule=child_i, context=data, comment=comment)
                child_dict[child_i[0]] = res
                pass

            return child_dict
        else:
            return data





if __name__ == "__main__":
    ciur3 = Ciur3("dsl/example.ciur")
    res =  ciur3.parse("http://google.com")
    import json
    print json.dumps(res, indent=4)
