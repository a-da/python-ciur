import re

input_data = """
root /jobs/job +
    title ./title str +
    url ./url str +1
    location . *
        country ./country str +1
        city ./city str +1
        zip ./postalcode ["str", "*1"]
"""


def parse(data):
    for number, line in enumerate(data.splitlines(), 1):
        line = line.strip()
        print ">_%s_" % line
        if not line:
            pass  # ignore
        else:
            m = re.search("^(\w+) ([\./a-zA-Z]+)$", line)
            if m:
                print "match"

parse(input_data)
