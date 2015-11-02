import re

input_data = """
root /jobs/job +
    title ./title str +
    url ./url str +1
    location . *
        country ./country str +1
        city ./city str +1
        zip ./postalcode str *1
"""

bnf = {
    "xpath": "(\.?(?:/\w+)*)",
    "type_list": "((?:str|int) )*[\+\*]\d+?)"
}


def parse(data):
    def _line(string, tab, parent):
        print "[INFO] string `%s`" % string
        if string == "":
            print "[INFO] ignore"
        else:
            # if start with indent then this is child

            pattern = "^%s([a-z]+) " % tab

            m = re.search(pattern, string)
            if not m:
                print string
                print "[ERROR] expect label on %s, see pattern `%s`" % ((number, 0), pattern)
                exit(1)
            name = m.group(1)

            return {
                "name": name,
            }

    rule = {}
    ret = None
    tab_ = ""
    for number, line in enumerate(data.splitlines(), 1):
        ret = _line(line, parent=ret, tab=tab_)
        rule["name"] = rule


parse(input_data)
