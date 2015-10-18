from ciur.dsl import get_bnf

test_res = [
    [['url', {'fragment': None, 'authority': 'stackoverflow.com', 'url': 'https://stackoverflow.com/questions/12565098/python-how-to-check-if-a-string-is-a-valid-iri?a=1', 'query': 'a=1', 'path': '/questions/12565098/python-how-to-check-if-a-string-is-a-valid-iri', 'scheme': 'https'}], ['name', 'exam plepage']],
    ['root', '/h3.1 ', ['node'], ' root commenter', [
        ['name', ".//h1[contains(text(), 'Justin')] ", ['str'], ' text'],
        ['count_list', ".//h2[contains(text(), 'Andrei')]/p ", ['list', 'int'], ' lala'],
        ['user', ".//h5[contains(text(), 'Andrei')]/p ", ['node'], [
            ['name', './spam ', ['str']],
            ['sure_name', './bold ', ['str']],
            ['age', './it ', ['int']],
            ['hobby', './li ', ['list', 'str']],
            ['indexes', './li/bold ', ['list', 'int']]
            ]
         ]
    ]
    ]
]


class Node(object):
    def __init__(self, xpath):
        xpath.strip()


class Ciur2(object):
    _lxml = "lxml"

    def __init__(self, file_):
        #bnf = get_bnf()
        #res = bnf.parseFile(file_, parseAll=True)
        res = test_res
        self._meta_url = res[0][0][1]
        self._meta_name = res[0][1][1]
        self._rules = res[1]

    def run(self):
        print self._rules[1]
        # noinspection PyTypeChecker
        page_context = Node("/")

        self._parse(page_context, self._rule, None)

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
    def _parse(self, context, rules, prev_rule=None):
        name = rules[0]
        xpath = rules[1]
        type_list = rules[2]
        next_rule = rules[3] if isinstance(rules[3], list) else rules[4]

        data = self._validate_type(type_list, context)

        if isinstance(data, Node):
            self._parse(data, self._rules[1:], rule)
        else:
            print "done2"

    # def _extract(self, context, xpath, name=None):
    #     if name in "root":
    #         return Node(xpath)
    #
    #     if name in "name":
    #         return "str"
    #
    #     if name in "user":
    #         return Node(xpath)


if __name__ == "__main__":
    ciur2 = Ciur2("dsl/example.ciur")
    ciur2.run()
