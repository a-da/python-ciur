import re

from lxml import etree
import lxml.etree


def regexp(context, item, *args):
    # print "==="
    # print type(context)
    # print args
    # print item
    # import time
    # time.sleep(0.1)
    # if len(item) > 1:
    #     raise NotImplementedError(item)

    # print(etree.ElementTree(context.context_node).getpath(context.context_node))

    if not item:
        #print "return none"
        return None

    text_list = []
    # noinspection PyProtectedMember
    if isinstance(item[0], lxml.etree._Element):
        for i_item in item:
            for i_item_text in i_item.xpath("./text()"):
                text_list.append(i_item_text)
    else:
        text_list = item

    tmp = []
    #print "text_list", text_list
    for i_text in text_list:
        # print "i_text", i_text
        # print "args", args
        # print "i_text", i_text
        # print "args[0]", args[0]
        #print ".........."
        #print "repr args[0], i_text, %s, %s" % (repr(args[0]), repr(i_text))
        m = re.search(args[0], i_text)
        #print "m", m
        if m:
            if len(args) == 1:
                tmp.append(m.group(0))
            else:
                for i_group in args[1:]:
                    #print "---- i_group", i_group
                    tmp.append(m.group(int(i_group)))

    #print "item %s, text_list: %s, args[0]: %s, tmp _%s_\n " % (item, text_list, args[0], tmp)

    if tmp:
        # print "return tmp"
        return tmp[0] if len(tmp) == 1 else tmp
    # elif text_list:
    #     return None

    return None
    #return context.context_node


def load():
    etree_functions = etree.FunctionNamespace("http://kjw.pt/xpath2-functions")
    etree_functions.prefix = "xp2f"

    etree_functions["regexp"] = regexp
