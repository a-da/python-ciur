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

input_data2 = """\
root ./jobs/job
    title ./title
    url ./url
    location .
        country ./country
        city ./city
        zip ./postalcode
"""


BNF = {
    "xpath": ".?(?:/\w+)*",
    "name": "\w+",
}
BNF["line"] = "%(name)s %(xpath)s" % BNF


def parse(data):
    """
    {
        "root": {
            "xpath": "/jobs/job",
            "type_list": ["+"],
            "rule": {
                "title" : {
                    "xpath": "./title",
                    "type_list": ["str", "+"]
                },
                "url" : {
                    "xpath": "./url",
                    "type_list": ["str", "+"]
                },
                "location" : {
                    "xpath": ".",
                    "type_list": ["*"],
                    "rule": {
                        "country" : {
                            "xpath": "./country",
                            "type_list": ["str", "+1"]
                        },
                        "city" : {
                            "xpath": "./city",
                            "type_list": ["str", "+1"]
                        },
                        "zip" : {
                            "xpath": "./postalcode",
                            "type_list": ["str", "*1"]
                        }
                    }
                }
            }
        }
    }
    """
    m = re.search("^%(line)s(\n {4}%(line)s)*" % BNF, data, re.DOTALL)
    print m.group(0)


parse(input_data2)
