# -*- coding: utf-8 -*-

import re
import json
import time
import html5lib
import datetime
import sre_constants

from lxml            import etree
from lxml.html.clean import clean_html
from HTMLParser      import HTMLParser
from ciur.common     import str_startswith
from lxml.etree      import _Element, _ElementStringResult, _ElementUnicodeResult, XMLSyntaxError, XPathEvalError, tostring

from ciur.util.AdvanceDictDomParser import AdvancedDictDomParser
from ciur.common import JsonException

class DomParserException(JsonException): pass


class DomParser(object):
    # TODO abstract functionality
    # TODO: $first get only first xpath match and ignore seconds
    # TODO: mandatory.list_len:<number>
    # TODO: mandatory.re_match:<name>
    """
    Abstract class for DOMParser child's
    `PRIMITIVES`
        // accept float, long, int, str, unicode, bool
        // accept only a list with one element
        int.
            min // get minimum form list
            max // get maximum from list

        // accept float, long, int, str, unicode, bool
        // accept only a list with one element
        float.
            round(<digit_number>)

        // accept float, long, int, str, unicode, bool
        // accept only a list with one element
        bool.

        // accept list, str, unicode, float, int, long, bool
        // accept a list or one element
        text.
            allow_empty_item // like [ None, "item2", None, "item3", "item4"]
            allow_empty_list // like [ ]
            force_list       // [ "one item" ]
            do_not_strip     // [ "   one item     ", "item two" ]
            join_by_space    // join list into string separated by " "
            join_by_new_line // join list into string separated by " "
            tail

        // raise error if element is null
        mandatory

        // skip that parent group item from list of parent item
        mandatory.skip

        // do not raise error if element is null
        optional

        // replace string
        ^replace:<name>
            where name define other rule
            - `from_str` or `from_re`
            - `to`
            - counts // how mush to repeat replace actions

        // extract some text from string with regexp
        ^drain:<name>
            where name define other rule
            - `re`
            - `group`

        // substitute string with its defined hash string
        ^hash_map:<name>
            where name define other rule
            - `map`
            - `default`
            - `separator`
            - `operator`
                in
                startswith
                endswith

        // if element can't be found set it into default value
        ^default:


        // get xml representation of dom with domains name
        ^xml:
            - args.pretty_print // True or False

        // get xml representation of dom without domains name
        ^html:
            - args.pretty_print // True or False

        // get inner html value
        // like `  <div>  <b>some value </b></div>  ` -> `<b>some value </b>`
        ^inner_html:

    `NODES`
        // ensure that returned result to be set in a list form
        ensure_list

        // raise error if element of node is null
        mandatory
    """
    # context
    # rules
    # anomalies
    # source
    # xpath
    # handlers
    html_parser = HTMLParser()


    def __init__(self, name, source, debug = False):
        self.name     = name
        self.source   = source
        self.debug    = debug
        self.handlers = {}
        self.xpath    = None

        if self.debug:
            print "constructor DOMParser"


    def __del__(self):
        if self.debug:
            print "destructor DOMParser"


    def validate_configs(self, configs):
        # TODO: check if comments have mandatory `#` preposition
        """
        #1 - check each xpath expression
        #2 - check casting chain
        """
        etree_object = html5lib.parse("<html>"
                                      "<head>d</head>"
                                      "<body>"
                                      "<div>some text hear</div>"
                                      "</body>"
                                      "</html>", treebuilder = "lxml")

        # TODO debug error for checking, after that decide to remove this is it needed
        #                                                               .xpath("/html:html/html:body",
        #                                                                     namespaces = {
        #                                                                         "html": "http://www.w3.org/1999/xhtml"
        #                                                                     })

        if not configs:
            raise DomParserException({
                "msg" : "Cant find config or config is null"
            })

        configs = AdvancedDictDomParser(configs)

        #-[1]------------------------------------
        # check json key configuration
        # key_name, allowed type
        mandatory_keys = {
            "blocks" : dict,
            "version" : int,
            "timestamp" : int,
            "config" : dict,
            "anomaly" : dict,
            "rules" : dict,
            "renames" : dict,
            "light_handlers" : dict
        }

        diff = set(mandatory_keys.keys()) ^ set(configs.keys())
        if diff:
            raise DomParserException({
                "msg" : "symmetric difference by keys",
                "expected_keys" : mandatory_keys.keys(),
                "config_keys" : configs.keys(),
                "diff" : list(diff)
            })

        for k, v in mandatory_keys.iteritems():
            if not configs.has_key(k):
                raise DomParserException({
                    "msg" : "missing mandatory key",
                    "key_name" : k,
                    "expected" : mandatory_keys
                })

            if not isinstance(configs[k], v):
                raise DomParserException({
                    "msg" : "wrong datatype initialization for key",
                    "key_name" : k,
                    "expected" : mandatory_keys
                })

        #-[2]------------------------------------
        # check light_handlers
        # key_name, allowed type
        for lh_key, lh_value in configs["light_handlers"].iteritems():
            allowed_ruled = [
                "^html:",
                "^xml:",
                "^inner_html:",
                "^replace:",
                "^drain:",
                "^hash_map:",
                "^default:"
            ]
            if not str_startswith(lh_key, allowed_ruled):
                raise DomParserException({
                    "msg" : "this rule are not allowed",
                    "key_name" : lh_key,
                    "allowed_rule" : allowed_ruled
                })

            if lh_key.startswith("^replace:"):
                for i_r in lh_value:
                    diff = set(i_r.keys()) - {"from_re", "from_str", "to", "counts", "comment"}
                    if diff:
                        raise DomParserException({
                            "msg" : "detected not allowed key name in light_handlers",
                            "diff" : list(diff),
                            "allowed_key" : ["from_re", "from_str", "to", "comment"]
                        })
                    if i_r.has_key("from_re"):
                        try:
                            i_r["from_re"] = re.compile(i_r["from_re"]) # compile regexp
                        except sre_constants.error, e:
                            raise DomParserException({
                                "msg" : "corrupted regexp in light_handler `^replace:`",
                                "key" : lh_key,
                                "regexp" : i_r["from_re"],
                                "detail" : e.message
                            })

            if lh_key.startswith("^drain:"):
                diff = set(lh_value.keys()) - {"re", "group"}
                if diff:
                    raise DomParserException({
                        "msg" : "detected not allowed key name in light_handler `^drain:`",
                        "diff" : list(diff),
                        "allowed_key" : ["re", "group"]
                    })

                try:
                    lh_value["re"] = re.compile(lh_value["re"]) # compile regexp
                except sre_constants.error, e:
                    raise DomParserException({
                        "msg" : "corrupted regexp in light_handlers",
                        "key" : lh_key,
                        "regexp" : lh_value["re"],
                        "group" : lh_value["group"],
                        "detail" : e.message
                    })


            if lh_key.startswith("^hash_map:"):
                diff = set(lh_value.keys()) - {"map", "default", "separator", "operator"}
                if diff:
                    raise DomParserException({
                        "msg" : "detected not allowed key name in light_handlers",
                        "diff" : list(diff),
                        "allowed_key" : ["map", "default"]
                    })

        #-[3]-------------------------------------
        # check conflicts light_headers vs headers
        diff = set(self.handlers) &  {i[1:] for i in configs["light_handlers"]}
        if diff:
            raise DomParserException({
                "msg" : "the same names was used in handlers and light_handlers",
                "diff" : list(diff)
            })


        def check_xpath_expression(expression, namespaces, key_path):
            # TODO fix bug for ignoring ./html:li[contain(text(), 'km')] instead of ./html:li[contain(text(), 'km')]
            """
            inner function  for `recursive_check`
            """
            if isinstance(expression, list):
                expression = "|".join(i for i in expression if not i.startswith("#"))

            if not (expression.startswith("/") or expression.startswith(".")):
                raise DomParserException({
                    "msg" : "Invalid xpath expression convention",
                    "xpath" : expression,
                    "key_path" : key_path,
                    "suggestion" : "put `.` or `/` before expression"
                })

            try:
                etree_object.xpath(expression, namespaces = namespaces)
            except XPathEvalError, e:
                if e.message in ("Invalid expression", "Invalid predicate", "Unfinished literal"):
                    raise DomParserException({
                        "msg" : e.message,
                        "xpath" : expression,
                        "key_path" : key_path
                    })
                elif e.message == "Undefined namespace prefix":
                    raise DomParserException({
                        "msg" : "Undefined namespace prefix",
                        "xpath" : expression,
                        "key_path" : key_path,
                        "namespaces" : namespaces
                    })
                else:
                    raise


        def recursive_check(root, key_path = ""):
            for k, v in root.iteritems():
                if k.startswith("#"): # ignore commented configs
                    continue

                tmp_key_path = key_path + "." + k
                v_len = v.__len__()
                if v_len == 2 or v_len == 3 and (isinstance(v[2], (str, unicode)) and not v[2].startswith("=>")):
                    # check chain_rules
                    r = set(v[0].split("|")) - {
                        "text.",
                        "float.",
                        "int.",
                        "bool",
                        "mandatory",
                        "mandatory.skip",
                        "optional",
                        "skip"
                    }
                    r_tmp = [ ]
                    for i_r in r:
                        if i_r.startswith("float."):
                            m = re.search("^float\.round_\d+$", i_r)
                            if m:
                                r_tmp.append(i_r)
                        elif i_r.startswith("int."):
                            m = re.search("^int\.(min|max)?$", i_r)
                            if m:
                                r_tmp.append(i_r)
                        elif i_r.startswith("text."):
                            m = re.search("^text\.("
                                          "allow_empty_item|"
                                          "allow_empty_list|"
                                          "force_list|"
                                          "join_by_space|"
                                          "join_by_new_line|"
                                          "tail"
                                          ")?$", i_r)
                            if m:
                                r_tmp.append(i_r)
                        elif i_r.startswith("^") and len(i_r) > 1:
                            r_tmp.append(i_r)

                    r -= set(r_tmp)
                    if r:
                        raise DomParserException({
                            "msg" : "invalid configs chain rule for primitives",
                            "chain_rule" : v[0],
                            "expected_chain_rule" : "text.|float.|int.|bool|mandatory|mandatory.skip|optional",
                            "key_path" : tmp_key_path,
                            "diff" : list(r)
                        })

                    check_xpath_expression(
                        expression = v[1],
                        namespaces = configs["config.xpath.namespaces"],
                        key_path   = tmp_key_path
                    )

                elif v_len == 3 and (isinstance(v[2], dict) or
                                     isinstance(v[2], (str, unicode)) and v[2].startswith("=>")):

                    if not isinstance(v[0], (str, unicode)):
                        raise DomParserException({
                            "msg" : "invalid data type for configs chain rule",
                            "chain_rule" : v[0],
                            "expected_type" : "string",
                            "key_path" : tmp_key_path
                        })
                    # check chain_rules
                    r = set(v[0].split("|")) - {"ensure_list", "mandatory", "optional"}
                    if r:
                        raise DomParserException({
                            "msg" : "invalid configs chain rule for nodes",
                            "chain_rule" : v[0],
                            "expected_chain_rule" : "text.|float.|int.|mandatory",
                            "key_path" : tmp_key_path,
                            "diff" : list(r)
                        })

                    check_xpath_expression(
                        expression = v[1],
                        namespaces = configs["config.xpath.namespaces"],
                        key_path   = tmp_key_path
                    )

                    if isinstance(v[2], (str, unicode)):
                        blocks_ref_key = v[2][2:]
                        if not configs["blocks"].has_key(blocks_ref_key):
                            raise DomParserException({
                                "msg" : "missed blocks_ref_key",
                                "blocks_ref_key" : blocks_ref_key,
                                "key_path" : tmp_key_path
                            })
                        else:
                            next_layer = configs["blocks"][blocks_ref_key]
                            v[2] = next_layer # overwrite with values from ref block
                    else:
                        next_layer = v[2]

                    recursive_check(next_layer, tmp_key_path)

                else:
                    raise DomParserException({
                        "msg" : "invalid configs rule item length or unexpected type data of node rule",
                        "length" : v_len,
                        "key_path" : tmp_key_path,
                        "type" : type(v[2] if v_len == 3 else None)
                    })

        recursive_check(configs["rules"])
        return True


    def save(self, js):
        """
        -save changes
        -increment current version number
        """
        if isinstance(js, (str, unicode)):
            # transform into object
            obj = json.loads(js)
        else:
            obj = js

        obj = AdvancedDictDomParser(obj)
        if not self.validate_configs(obj):
            raise Exception("config can't be validated ```%s```" %obj.get)

        if not self.context:
            # create new one
            self.context = {
                "name" : self.name,
                "version" : 0,
                "versions" : []
            }
        else:
            #use old context
            pass

        self.context = AdvancedDictDomParser(self.context)
        self.context["version"] = self.context["versions"].__len__() + 1

        self.validate_configs(obj)
        obj["version"]   = self.context["version"]
        obj["timestamp"] = int(time.time())
        obj["datetime"]  = str(datetime.datetime.now())
        self.context["versions"].append(obj)


    def get_version(self, version="default"):
        """
        get xpath
        if version is not specified then get active
        """

        version_number = self.context["version"] if version == "default" else version

        tmp = None
        if self.context["versions"]:
            tmp = self.context["versions"][version_number - 1]
            tmp = AdvancedDictDomParser(tmp)

        return tmp


    def get_version_size(self):
        return self.context["versions"].__len__()


    @staticmethod
    def __int(casting_rule, value):
        # TODO casting_rule
        """
        convert into int
        """

        if isinstance(value, list):
            value = [i for i in value if not (isinstance(i, _Element) and i.text == None)] # do not optimise

        if not value: # None
            return value

        if isinstance(value, (float, long, int, str, unicode, bool)):
            try:
                value = int(value)
                return value
            except ValueError, e:
                raise DomParserException({
                    "msg" : e.message,
                    "suggestion" : "tried to make convert for only one item and expected to be int",
                    "code" : "__int"
                })


        v_len = value.__len__()

        if not v_len:
            return None

        tmp_value = [ ]
        for i_value in value:
            if isinstance(i_value, _Element):
                i_value = i_value.text
            try:
                i_value = int(i_value, 0)
            except ValueError, e:
                if e.message.startswith("invalid literal for int() with base 0:"):
                    raise DomParserException({
                        "msg" : e.message,
                        "suggestion" : "tried to make convert for more than one item and expected to be int",
                        "code" : "__int"
                    })
                else:
                    raise

            tmp_value.append(i_value)
        value = tmp_value

        if casting_rule == "int.max":
            return max(value)

        if casting_rule == "int.min":
            return min(value)

        if len(value) == 1 and (value[0] == 0 or value[0]):
            return value[0]

        return value


    @staticmethod
    def __float(casting_rule, value):
        # TODO casting_rule
        """
        casting into float
        """

        if isinstance(value, list):
            value = [i for i in value if not (isinstance(i, _Element) and i.text == None)] # do not optimise

        if not value: # None
            return value

        if isinstance(value, (float, long, int, str, unicode, bool)):
            value = int(value)
            return value

        v_len = value.__len__()
        if not v_len:
            return None

        if v_len > 1:
            raise DomParserException({
                "msg" : "undesired behavior, xpath int should have only one item but have `%d` items" %v_len,
                "code" : "__float"
            })

        value = value[0]
        value = value.text
        value = float(value)

        m = re.search(".round_(\d)", casting_rule)
        if m:
            value = round(value, int(m.group(1)))

        return value


    @staticmethod
    def __bool(value):
        # TODO casting_rule
        """
        casting into int
        """

        if isinstance(value, list):
            value = [i for i in value if not (isinstance(i, _Element) and i.text == None)] # do not optimise

        if not value and not isinstance(value, (float, int, long, bool)):
            return False

        if isinstance(value, (float, long, int, bool)):
            value = int(value)
            return value
        elif isinstance(value, (unicode, str)):
            value = value.strip()
            if value.lower() == "false" or value == "":
                return False
            return True

        v_len = value.__len__()
        if not v_len:
            return None

        if v_len > 1:
            raise DomParserException({
                "msg" : "undesired behavior, xpath int should have only one item but have `%d` items" %v_len,
                "code" : "__float"
            })

        value = value[0]
        if not isinstance(value, _ElementStringResult):
            value = value.text

        if value.lower() == "false":
            return False

        return True

    @classmethod
    def __text(cls, casting_rule, value):
        """
        casting into text
        text.(allow_empty_item?|allow_empty_list?|force_list?)?
        allow_empty_item: ["", "ddd"]
        allow_empty_list: [ ]
        force_list: "text" -> ["text"]
        default:
            don't allow empty item and empty list
            if result is list with one item return only this item
        """
        flag_allow_empty_item = False
        flag_allow_empty_list = False
        flag_force_list       = False
        flag_do_not_strip     = False
        flag_join_by_space    = False
        flag_join_by_new_line = False
        flag_tail             = False
        for flag in casting_rule.split(".")[1:]:
            if flag == "allow_empty_item":
                flag_allow_empty_item = True
            if flag == "allow_empty_list":
                flag_allow_empty_list = True
            if flag == "force_list":
                flag_force_list = True
            if flag == "do_not_strip":
                flag_do_not_strip = True
            if flag == "join_by_space":
                flag_join_by_space = True
            if flag == "join_by_new_line":
                flag_join_by_new_line = True
            if flag == "tail":
                flag_tail = True

        if not isinstance(value, list):
            value = [value]

        value_list = [ ]
        for i_value in value:
            if isinstance(i_value, (float, long, int, bool)):
                i_value = str(i_value)
            else:
                if not isinstance(i_value, (_ElementStringResult, _ElementUnicodeResult)):
                    if flag_tail:
                        i_value = i_value.tail
                    else:
                        i_value = i_value.text

                if not isinstance(i_value, (str, unicode)):
                    i_value = i_value.text


                if not flag_do_not_strip and i_value:
                    i_value = i_value.strip()

            if flag_allow_empty_item or i_value:
                value_list.append(i_value)

        value = value_list

        # unescape from <iPad&#039;s>  to <Ipad's>
        length = len(value)
        while length:
            length -= 1
            if isinstance(value[length], (str, unicode)):
                value[length] = cls.html_parser.unescape(value[length])

        if flag_allow_empty_list or value:
            if not flag_force_list and isinstance(value, list) and value.__len__() == 1 and not flag_allow_empty_item:
                value = value[0]
            elif flag_force_list and not isinstance(value, list):
                value = [value]
        else:
            value = None


        if value and isinstance(value, list):
            if flag_join_by_space:
                value = " ".join(value)
                value = re.sub("\s*([\.,;\)\]\}])\s*", lambda x: x.group(1) + " ", value)
                value = re.sub("\s+", " ", value)
                value = value.strip()

            if flag_join_by_new_line:
                value = "\n".join(value)

        return value


    def __children_nodes(self, casting_rule, value, children_rule, key_path):
        """
        handle nodes
        """
        flag_ensure_list = False
        flag_mandatory   = False
        for i_cast in casting_rule.split("|"):
            if i_cast == "ensure_list":
                flag_ensure_list = True
            if i_cast == "mandatory":
                flag_mandatory = True
            if i_cast == "optional":
                pass

        tmp_list = [ ]
        for i_value in value:
            tmp = self.__dive_next_level([i_value], children_rule, key_path)
            if tmp:
                tmp_list.append(tmp)

        tmp = None
        if not flag_ensure_list:
            if isinstance(tmp_list, list) and len(tmp_list) == 1:
                tmp = tmp_list[0]
            else:
                tmp = tmp_list
        else:
            if not isinstance(tmp_list, list):
                tmp = [tmp_list]
            else:
                tmp = tmp_list

        if not tmp and flag_mandatory:
            raise DomParserException({
                "key_path" : key_path,
                "msg" : "Require mandatory elements from children",
                "code" : "__dive_next_level"
            })

        return tmp

    @staticmethod
    def __replace_by_light_handlers(value, replace_rule):
        """
        handle `replace` inline function declarations from jxpath
        """
        def _fun_replace(v):
            for i_rr in replace_rule:
                v = v.strip()
                if not v: break
                counts = i_rr.get("counts", 1)
                while counts:
                    counts -= 1
                    if i_rr.has_key("from_str"):
                        v = v.replace(i_rr["from_str"], i_rr["to"])
                    elif i_rr.has_key("from_re"):
                        v = i_rr["from_re"].sub(i_rr["to"], v)
                    else:
                        raise DomParserException({
                            "msg" : "can't detected replace key `from`",
                            "keys" : i_rr,
                            "expected" : ["from_re", "from_str"]
                        })
            return v

        if not value:
            pass # skip
        elif isinstance(value, list):
            value = map(_fun_replace, value)
        else: #str
            value = _fun_replace(value)

        return value


    @staticmethod
    def __drain_by_light_handlers(value, drain_rule):
        # TODO write doctests
        """
        handle `drain` inline function declarations from jxpath
        """
        def _drain(v):
            v = v.strip()
            m = drain_rule["re"].search(v)
            if not m:
                return None
            v = m.group(drain_rule["group"])
            return v

        if not value:
            pass # skip
        elif isinstance(value, list):
            value = map(_drain, value)
        else: #str
            value = _drain(value)

        return value


    @staticmethod
    def __hash_map_by_light_handlers(value, replace_rule):
        # TODO multiply key subitems by separators
        """
        get map equivalent for string items
        """
        def _f(v):
            if not isinstance(v, (str, unicode)):
                raise DomParserException({
                    "msg" : "expected only string or unicode format",
                    "received_type" : str(type(v))
                })

            if v in replace_rule["map"]:
                return replace_rule["map"][v]
            else:
                # check in key name by separators
                # remove after implement TODO
                operator = replace_rule.get("operator")
                if operator not in ["in", "startswith", "endswith"]:
                    raise DomParserException({
                        "msg" : "expected hash_map.operator in [in, startswith, endswith]",
                        "received_type" : operator
                    })

                if operator == "in":
                    for  k_map in replace_rule["map"]:
                        if v in k_map.split(replace_rule["separator"]):
                            return replace_rule["map"][k_map]
                elif operator == "startswith":
                    for  k_map in replace_rule["map"]:
                        for i_splited in k_map.split(replace_rule["separator"]):
                            if v.startswith(i_splited):
                                return replace_rule["map"][k_map]
                elif operator == "endswith":
                    for  k_map in replace_rule["map"]:
                        for i_splited in k_map.split(replace_rule["separator"]):
                            if v.endswith(i_splited):
                                return replace_rule["map"][k_map]

                if not replace_rule["default"]:
                    return v
                else:
                    return replace_rule["default"]

        if not value:
            pass # skip
        elif isinstance(value, list):
            value = map(_f, value)
        else: #str
            value = _f(value)

        return value


    @staticmethod
    def __default_by_light_handlers(value, replace_rule):
        """
        set default value
        """
        def _f(v):
            if not v:
                if isinstance(v, (int, bool, float, long)):
                    return v
                else:
                    return replace_rule
            return v

        if not value:
            return replace_rule

        if isinstance(value, list):
            value = map(_f, value)
        else: #str
            value = _f(value)

        return value


    @staticmethod
    def __xml_by_light_handlers(value, args):
        """
        handle `xml` inline function declarations from jxpath
        """
        def _f(v):
            v = tostring(
                v, method="html", pretty_print = args.get("pretty_print")
                # TODO find out purposed of `inclusive_ns_prefixes`
                )
            return v

        if isinstance(value, list):
            value = map(_f, value)
        else: #str
            value = _f(value)

        return value


    @classmethod
    def __html_by_light_handlers(cls, value, args):
        """
        handle `html` inline function declarations from jxpath
        """
        res = cls.__xml_by_light_handlers(value, args)

        def _f(v):
            v = v.replace(' xmlns:html=\"http://www.w3.org/1999/xhtml\">', ">")
            v = v.replace(' xmlns:html=\"http://www.w3.org/1999/xhtml\" ', " ")
            v = v.replace("<html:", "<")
            v = v.replace("</html:", "</")
            return v

        if type(res) == list:
            res = map(_f, res)
        else:
            res = _f(res)

        return res


    @staticmethod
    def __strip_tag_block(block):
        """
        inner function for __extract_content_tags
        """
        remove_beg = re.compile("^(&nbsp;|\s*|&#160)")
        remove_end = re.compile("(&nbsp;|\s*|&#160)$")

        # strip
        while True:
            len_b = len(block)
            block = remove_beg.sub("", block)
            block = remove_end.sub("", block)
            len_a = len(block)
            if len_b == len_a:
                break

        return block


    @classmethod
    def __extract_content_tags(cls, block):
        """
        inner function for __inner_html_by_light_handlers
        """
        beg_tag = re.compile("^<\s*([^>]+?)( +[^>]+)?\s*>\s*")
        end_tag = re.compile("\s*<\s*/([^>]+)\s*>\s*$")
        block = cls.__strip_tag_block(block)
        # -[2]- extract tags
        m = beg_tag.search(block)
        if m:
            open_tag = m.group(1)
        else:
            raise Exception({
                "msg" : "can't find open tag",
                "tags_block" : block
            })

        m = end_tag.search(block)
        if m:
            close_tag = m.group(1)
        else:
            raise Exception({
                "msg" : "can't find close tag",
                "tags_block" : block
            })

        if open_tag != close_tag:
            raise Exception({
                "msg" : "open and close tag are different",
                "tags_block" : block,
                "open_tag" : open_tag,
                "close_tag" : close_tag
            })

        block = beg_tag.sub("", block)
        block = end_tag.sub("", block)
        return block

    @classmethod
    def __inner_html_by_light_handlers(cls, value, args):
        """
        handle `inner_html` inline function declarations from jxpath
        """
        value = cls.__html_by_light_handlers(value, args)
        if isinstance(value, list):
            value = map(cls.__extract_content_tags, value)
        else:
            value = cls.__extract_content_tags(value)

        return value


    def __dive_next_level(self, xp_root_node, rules, parent_key = ""):
        """
        `casting_chain`
        mandatory|optional
        """
        m = AdvancedDictDomParser()

        for xp_result_item in xp_root_node:
            for k_rule, v_rule in rules.iteritems():
                key_path = parent_key + "." + k_rule

                if k_rule.startswith("#"): # skip commented field
                    continue

                casting_chain = v_rule[0]

                xpath_express = "|".join(i for i in v_rule[1] if not i.startswith("#")) if isinstance(v_rule[1], list) \
                    else v_rule[1]

                comments = False

                if (len(v_rule) == 3 and isinstance(v_rule[2], (str, unicode))) or len(v_rule) == 2 :
                    comments = True

                # TODO remove try/except after fix bug in checking
                try:
                    value = xp_result_item.xpath(xpath_express, namespaces = self.xpath["config.xpath.namespaces"])
                except XPathEvalError, e:
                    raise DomParserException({
                        "msg" : e.message,
                        "xpath" : xpath_express,
                        "key_path" : key_path
                    })

                if comments: # have no children nodes

                    for i_casting_chain in casting_chain.lower().split("|"):
                        if i_casting_chain == "mandatory":
                            if not (isinstance(value, (bool, int, float, long)) or value): #! do not change (ignore bool)
                                raise DomParserException({
                                    "key_path" : key_path,
                                    "msg" : "Require mandatory elements from data type",
                                    "code" : "__dive_next_level"
                                })
                            # else: is ok

                        elif i_casting_chain == "mandatory.skip":
                            if not value:
                                return AdvancedDictDomParser()

                        elif i_casting_chain == "optional":
                            pass

                        elif i_casting_chain.startswith("text."):
                            value = self.__text(i_casting_chain, value)

                        elif i_casting_chain.startswith("bool"):
                            value = self.__bool(value)

                        elif i_casting_chain.startswith("int."):
                            value = self.__int(i_casting_chain, value)

                        elif i_casting_chain.startswith("float."):
                            value = self.__float(i_casting_chain, value)

                        elif i_casting_chain == "skip":
                            value = self.__text("text.", value)
                            if value:
                                return AdvancedDictDomParser()

                        elif i_casting_chain.startswith("^"):
                            if i_casting_chain[1:] in self.handlers:
                                value = self.handlers[i_casting_chain[1:]](value)

                            elif i_casting_chain in self.xpath["light_handlers"]:
                                if i_casting_chain.startswith("^replace:"):
                                    value = self.__replace_by_light_handlers(
                                        value,
                                        self.xpath["light_handlers"][i_casting_chain]
                                    )
                                elif i_casting_chain.startswith("^drain:"):
                                    value = self.__drain_by_light_handlers(
                                        value,
                                        self.xpath["light_handlers"][i_casting_chain]
                                    )
                                elif i_casting_chain.startswith("^hash_map:"):
                                    value = self.__hash_map_by_light_handlers(
                                        value,
                                        self.xpath["light_handlers"][i_casting_chain]
                                    )

                                elif i_casting_chain.startswith("^default:"):
                                    value = self.__default_by_light_handlers(
                                        value,
                                        self.xpath["light_handlers"][i_casting_chain]
                                    )

                                elif i_casting_chain.startswith("^xml:"):
                                    value = self.__xml_by_light_handlers(
                                        value,
                                        self.xpath["light_handlers"][i_casting_chain]
                                    )

                                elif i_casting_chain.startswith("^html:"):
                                    value = self.__html_by_light_handlers(
                                        value,
                                        self.xpath["light_handlers"][i_casting_chain]
                                    )

                                elif i_casting_chain.startswith("^inner_html:"):
                                    value = self.__inner_html_by_light_handlers(
                                        value,
                                        self.xpath["light_handlers"][i_casting_chain]
                                    )

                                else:
                                    raise DomParserException({
                                        "key_path" : key_path,
                                        "msg" : "unknown light handler function prefix",
                                        "i_casting_chain" : i_casting_chain,
                                        "light_handlers" : self.xpath["light_handlers"].keys()
                                    })
                            else:
                                raise DomParserException({
                                    "key_path" : key_path,
                                    "msg" : "unknown data type/rule from inline functions",
                                    "i_casting_chain" : i_casting_chain,
                                    "casting_chain" : casting_chain
                                })
                        else:
                            raise DomParserException({
                                "key_path" : key_path,
                                "msg" : "unknown data type/rule from casting_chain",
                                "i_casting_chain" : i_casting_chain,
                                "casting_chain" : casting_chain,
                                "code" : "__dive_next_level"
                            })

                    tmp = value

                else: # have children nodes
                    tmp = self.__children_nodes(
                        casting_rule = casting_chain,
                        value = value,
                        children_rule = v_rule[2],
                        key_path = key_path
                    )

                m.dom_push(k_rule, tmp)

        return m


    def set_handlers(self, handlers):
        self.handlers = dict([ (i.__name__, i) for i in handlers])


    def __dive_root_level(self, xpath_result):
        len_xp_result = len(xpath_result)

        if len(xpath_result) != 1:
            raise DomParserException({
                "msg" : "Failed root detection",
                "xpath_expression" : self.xpath["config.xpath.root"],
                "roots_numbers" : len_xp_result
            })

        result = self.__dive_next_level(xpath_result, self.xpath["rules"])

        if type(result) == list and len(result) == 1:
            result = result[0]

        return result


    def dive_xml_root_level(self, xml,  handlers = None):
        if handlers:
            self.set_handlers(handlers)

        if not self.xpath:
            self.xpath = self.get_version()

        etree_xml = None
        if isinstance(xml, (str, unicode)):
            try:
                etree_xml = etree.XML(xml)
            except XMLSyntaxError, e:
                raise DomParserException({
                    "msg" : e.message,
                    "xml" : xml,
                    "suggestion" : "possible is plain/text not xml"
                })

            if xml.startswith(
                '﻿<?xml version="1.0" encoding="utf-8"?>\r\n' +
                '<feed xml:lang="tr-TR" xmlns="http://www.w3.org/2005/Atom">'):
                etree_xml = [etree_xml]

        if not len(etree_xml):
            raise DomParserException({
                "msg" : "xml is not str or unicode or failed initialisation",
                "type_xml" : type(xml),
                "val_xml" : xml
            })

        result = self.__dive_root_level(xpath_result=etree_xml)
        return result


    def dive_html_root_level(self, html, to_clean = False, handlers = None, disable_br = True, disable_hr = False):

        if handlers:
            self.set_handlers(handlers)

        if not self.xpath:
            self.xpath = self.get_version()

        if isinstance(html, (str, unicode)):
            if to_clean: # TODO fix unicode corrupted conversion
                html = clean_html(html)

            if disable_br:
                html = re.sub("(?i)\s*<\s*br\s*/?\s*>\s*", "\n", html)

            if disable_hr:
                html = re.sub("(?i)\s*<\s*hr\s*/?\s*>\s*", "\n", html)

            try:
                xp_root = html5lib.parse(html, treebuilder = "lxml")
            except ValueError,e:
                if self.debug:
                    print "[WARNING] html5lib->", e.message
                html = html.decode("utf-8")
                for i_char_code in [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19,
                          18, 17, 16, 15, 14, 11, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if unichr(i_char_code) in html:
                        if self.debug:
                            print "[WARNING] remove BAD char code `%d` from html" %i_char_code
                        html = html.replace(unichr(i_char_code), "")

                xp_root = html5lib.parse(html, treebuilder = "lxml")

            xp_result = xp_root.xpath(
                _path = self.xpath["config.xpath.root"],
                namespaces = self.xpath["config.xpath.namespaces"]
            )
        else:
            xp_result = html

        result = self.__dive_root_level(xp_result)

        return result


class DomParserObjectJson(DomParser):
    """
    Json object implimentation of DomParser
    1. Got xjson json object
    2. Got page string
    3. return desired data form parsed page into json format
    """
    pass


class DomParserUrl(DomParser):
    """
    Remote implimentation of DomParser
    1. Got xjson from links
    2. Got page from link
    3. return desired data form parsed page into json format
    """
    pass


class DomParserSQLite(DomParser):
    """
    Database SQLite implimentation of DomParser
    1. Got xjson from Database SQLite
    2. Got page *
    3. return desired data form parsed page into json format
    """
    pass

class DomParserMySQL(DomParser):
    """
    Database MySQL implimentation of DomParser
    1. Got xjson from Database MySQL
    2. Got page *
    3. return desired data form parsed page into json format
    """
    pass


class DomParserMongoDb(DomParser):
    """
    Database MongoDb implimentation of DomParser
    1. Got xjson from Database MongoDb
    2. Got page *
    3. return desired data form parsed page into json format
    """
    pass
