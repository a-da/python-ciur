# -*- coding: utf-8 -*-
from __future__ import print_function

import re
import datetime
import json
import time
import sre_constants

import html5lib
from lxml import etree
from lxml.html.clean import clean_html
from lxml.etree import XMLSyntaxError
from lxml.etree import XPathEvalError

from ciur.util import AdvancedDictDomParser
from ciur.common import JsonException
from ciur.common import InlineHandlers
from ciur.common import str_startswith


class DomParserException(JsonException):
    pass

# TODO
"""
    add set feature unique value in list

    "repolist" : ["optional", "//div[@class='repo-tab']//ul[@class='repo-stats']", {
                "#lang" : ["text.|optional", "/li[not(@class)]"],
                "#stargazers" : ["text.tail|mandatory", "/li[@class='stargazers']/a/span"],
                "_forks" : ["text.tail|mandatory", "./li[@class='forks']/a/span"],
                "forks"  : ["^html:|mandatory", "./li[@class='forks']/a"],
                "#name" : ["text.|mandatory", "../h3/a"]
            }]

     "_forks" : ["text.tail|mandatory", "/li[@class='forks']/a/span"],

    without dot will throw error
"""


class DomParser(object):
    # TODO abstract functionality
    # TODO: $first get only first xpath match and ignore seconds
    # TODO: mandatory.list_len:<number>
    # TODO: mandatory.re_match:<name>
    # TODO: ^between : [<lower>, <top>]
    # TODO: ^in : [<i1>, <i2>, .., <in2>]
    # TODO: ^ensure_count
    # TODO: make absolute url
    # TODO: force_list for node
    # TODO:  fix bug "name" : ["text.|mandatory", "//h3/a"]
    #  File "/code5/my/lib/ciur/common/dom_parser.py", line 209, in _check_primitives_chain_rules
    # raise NotImplemented
    # TypeError: exceptions must be old-style classes or derived from BaseException, not NotImplementedType
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
            has_comma_sep like "84,57" instead of "84.57", if has dot separator instead of comma separator raise error


        // accept float, long, int, str, unicode, bool
        // accept only a list with one element
        bool.

        // remove duplicates from list
        set.

        // accept list, str, unicode, float, int, long, bool
        // accept a list or one element
        text.
            allow_empty_item // like [ None, "item2", None, "item3", "item4"]
            allow_empty_list // like [ ]
            force_list       // [ "one item" ]
            do_not_strip     // [ "   one item     ", "item two" ]
            join_by_space    // join list into string separated by " "
            join_by_new_line // join list into string separated by " "
            tail             // get only tail
            with_tail        // get text element with tail TODO
            skip             // if found such text skip parsing other fragments and return empty item

        // raise error if element is null
        mandatory
            // skip that parent group item from list of parent item
            mandatory.skip

        // do not raise error if element is null
        optional

        // replace string
        ^replace:<name>
            [
                {
                    - `from_str` or `from_re`
                    - `to`
                    - counts // how mush to repeat replace actions
                }
            ]

        // extract some text from string with regexp
        ^drain:<name>
            where name define other rule
            {
                - `re`
                - `group`
            }

        // parse date from string http://docs.python.org/library/datetime.html#strftime-and-strptime-behavior
        ^date:<name>
            [ list_of_date_string_formats ]


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

            samples:
            * "^html:some_name": {"pretty_print" : true}
            * "^html:another_name": {"pretty_print" : false}  equivalent to "^html:another_name": {}

        // get inner html value
        // like `  <div>  <b>some value </b></div>  ` -> `<b>some value </b>`
        ^inner_html:

    `NODES`
        // ensure that returned result to be set in a list form
        ensure_list

        // raise error if element of node is null
        mandatory

    more info about xpath:
        - http://msdn.microsoft.com/en-us/library/ms256086.aspx
        - http://www.w3.org/TR/xpath/
        - http://www.w3schools.com/xpath/xpath_operators.asp
        - http://xpath.alephzarro.com/content/cheatsheet.html#chRegExp
        - http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.help.ase_15.0.xmlb/html/xmlb/xmlb32.htm
        TODO look at to toUpper and union,

    """
    # context
    # rules
    # anomalies
    # source
    # xpath
    # handlers

    def __init__(self, name, source, debug=False):
        self.name = name
        self.source = source
        self.debug = debug
        self.handlers = {}
        self.xpath = None

        if self.debug:
            print("[INFO] constructor DOMParser")

    def __del__(self):
        if self.debug:
            print("[INFO] destructor DOMParser")

    @staticmethod
    def _check_primitives_chain_rules(chain_rules):
        # check chain_rules
        rule_list = [
            "text.",
            "float.",
            "int.",
            "bool.",
            "mandatory",
            "mandatory.skip",
            "optional",
            "set."
        ]

        diff_rules = set(chain_rules.split("|")) - set(rule_list)
        r_tmp = []
        for i_rule in diff_rules:
            if i_rule.startswith("float."):
                m = re.search("^float\.(round_\d+|has_comma_sep)$", i_rule)
                if m:
                    r_tmp.append(i_rule)

            elif i_rule.startswith("int."):
                m = re.search("^int\.(min|max)?$", i_rule)
                if m:
                    r_tmp.append(i_rule)

            elif i_rule.startswith("text."):
                text_dot_list = [
                    "allow_empty_item",
                    "allow_empty_list",
                    "force_list",
                    "join_by_space",
                    "join_by_new_line",
                    "with_tail",
                    "tail"
                ]

                postfix = i_rule[len("text."):]
                for i_postfix in text_dot_list:
                    if postfix == i_postfix:
                        r_tmp.append(i_rule)
                        break
                else:
                    raise DomParserException({
                        "msg": "NotImplemented",
                        "rule": i_rule,
                        "expect": text_dot_list
                    })


            elif i_rule.startswith("^") and len(i_rule) > 1:
                r_tmp.append(i_rule)

            else:
                raise DomParserException({
                    "msg": "NotImplemented",
                    "rule": i_rule
                })

        diff_rules = list(diff_rules - set(r_tmp))
        if diff_rules:
            raise DomParserException({
                "msg": "invalid configs chain rule for primitives",
                "chain_rule": chain_rules,
                "expected_chain_rule": rule_list,
                "diff": list(diff_rules)
            })

    @staticmethod
    def _check_nodes_chain_rules(chain_rules):
        rules_list = ["ensure_list", "mandatory", "optional"]

        diff_rules = list(set(chain_rules.split("|")) - set(rules_list))
        if diff_rules:
            raise DomParserException({
                "msg": "invalid configs chain rule for nodes",
                "chain_rule": chain_rules,
                "expected_chain_rule": rules_list,
                "diff": diff_rules
            })

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
                "msg": "Cant find config or config is null",
                "source": self.source
            })

        configs = AdvancedDictDomParser(configs)

        #-[1]------------------------------------
        # check json key configuration
        # key_name, allowed type
        mandatory_keys = {
            "blocks": dict,
            "version": int,
            "timestamp": int,
            "config": dict,
            "anomaly": dict,
            "rules": dict,
            "reformat": list,
            "light_handlers": dict,
            "bad_character_list": list
        }

        diff = set(mandatory_keys.keys()) ^ set(configs.keys())
        if diff:
            raise DomParserException({
                "msg": "symmetric difference by keys",
                "expected_keys": mandatory_keys.keys(),
                "config_keys": configs.keys(),
                "diff": list(diff)
            })

        for k, v in mandatory_keys.iteritems():
            if k not in configs:
                raise DomParserException({
                    "msg" : "missing mandatory key",
                    "key_name" : k,
                    "expected" : mandatory_keys
                })

            if not isinstance(configs[k], v):
                raise DomParserException({
                    "msg": "wrong datatype initialization for key",
                    "key_name": k,
                    "expected": mandatory_keys
                })

        #-[2]------------------------------------
        # check light_handlers
        # key_name, allowed type
        for lh_key, lh_value in configs["light_handlers"].iteritems():
            allowed_ruled = InlineHandlers._get_methods()

            if not str_startswith(lh_key, *allowed_ruled):
                raise DomParserException({
                    "msg": "this rule are not allowed",
                    "key_name": lh_key,
                    "allowed_rule": allowed_ruled
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
                    if "from_re" in i_r:
                        try:
                            i_r["from_re"] = re.compile(i_r["from_re"]) # compile regexp
                        except (sre_constants.error,) as e:
                            raise DomParserException({
                                "msg" : "corrupted regexp in light_handler `^replace:`",
                                "key" : lh_key,
                                "regexp" : i_r["from_re"],
                                "detail" : e.message
                            })

            if lh_key.startswith("^drain:"):
                if not isinstance(lh_value, dict):
                    raise DomParserException({
                        "msg": "wrong data type in `^drain`",
                        "got": lh_value,
                        "expect" : dict
                    })

                diff = set(lh_value.keys()) - {"re", "group"}
                if diff:
                    raise DomParserException({
                        "msg" : "detected not allowed key name in light_handler `^drain:`",
                        "diff" : list(diff),
                        "allowed_key" : ["re", "group"]
                    })

                try:
                    lh_value["re"] = re.compile(lh_value["re"]) # compile regexp
                except (sre_constants.error, ) as e:
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
                "msg": "the same names was used in handlers and light_handlers",
                "diff": list(diff)
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
                etree_object.xpath(expression, namespaces=namespaces)
            except (XPathEvalError, ) as e:
                if e.message in ("Invalid expression", "Invalid predicate", "Unfinished literal"):
                    raise DomParserException({
                        "msg": e.message,
                        "xpath": expression,
                        "key_path": key_path
                    })
                elif e.message == "Undefined namespace prefix":
                    raise DomParserException({
                        "msg": "Undefined namespace prefix",
                        "xpath": expression,
                        "key_path": key_path,
                        "namespaces": namespaces
                    })
                else:
                    raise

        def recursive_check(root, key_path = ""):
            # astrix handling `for_each`
            if "*" in root:
                v = root["*"]
                if isinstance(v[1], dict):
                    len_v = len(v)
                    for_ = v[1]["for"]

                    if "{0}" not in v[1]["in"]:
                        raise  DomParserException({
                            "msg" : "astrix patter should contain at least on `{0}` symbol",
                            "got" : v[1]["in"]
                        })

                    if isinstance(for_, dict):
                        for k_for, v_for in for_.iteritems():
                            if not isinstance(v_for, basestring):
                                raise  DomParserException({
                                    "msg": "wrong type for `*` rule",
                                    "got": repr(v_for),
                                    "expected": "basestring"
                                })

                            if len_v == 3:
                                root[k_for.lower()] = [v[0], v[1]["in"].format(v_for), v[2]]
                            else: # len_v == 2
                                root[k_for.lower()] = [v[0], v[1]["in"].format(v_for)]

                    elif isinstance(for_, list):
                        for item in for_:
                            if not isinstance(item, basestring):
                                raise  DomParserException({
                                    "msg": "wrong type for `*` rule",
                                    "got": repr(item),
                                    "expected": basestring
                                })

                            if len_v == 3:
                                root[item.lower()] = [v[0], v[1]["in"].format(item), v[2]]
                            else: # len_v == 2
                                root[item.lower()] = [v[0], v[1]["in"].format(item)]
                    else:
                        raise NotImplemented

                    del root["*"]
            else:
                for k, v in root.iteritems():
                    if isinstance(v[1], dict):
                        raise DomParserException({
                            "msg" : "expect to be astrix notation in key",
                            "v" : v,
                            "k" : k
                        })


            for k, v in root.iteritems():
                if k.startswith("#"): # ignore commented configs
                    continue

                tmp_key_path = key_path + "." + k
                v_len = len(v)

                if v_len not in [2, 3]:
                    raise NotImplemented

                if not isinstance(v[0], basestring):
                    raise DomParserException({
                        "msg"           : "invalid data type for configs chain rule",
                        "chain_rule"    : v[0],
                        "expected_type" : "string",
                        "key_path"      : tmp_key_path
                    })

                if v_len == 3 and isinstance(v[2], basestring):
                    if v[2].startswith("=>"):
                        blocks_ref_key = v[2][2:]
                        if blocks_ref_key not in configs["blocks"]:
                            raise DomParserException({
                                "msg"            : "missed blocks_ref_key",
                                "blocks_ref_key" : blocks_ref_key,
                                "key_path"       : tmp_key_path
                            })

                        v[2] = configs["blocks"][blocks_ref_key]
                    elif not v[2].startswith("#"):
                        raise NotImplemented

                if v_len == 2 or (v_len == 3 and isinstance(v[2], basestring)):
                    self._check_primitives_chain_rules(v[0])

                elif v_len == 3 and isinstance(v[2], dict):
                    self._check_nodes_chain_rules(v[0])
                    recursive_check(v[2], tmp_key_path)

                else:
                    check_xpath_expression(
                        expression = v[1],
                        namespaces = configs["config.xpath.namespaces"],
                        key_path   = tmp_key_path
                    )

        recursive_check(configs["rules"])
        return True


    def save(self, js):
        """
        -save changes
        -increment current version number
        """
        if isinstance(js, basestring):
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


    def _children_nodes(self, casting_rule, value, children_rule, key_path):
        """
        handle nodes
        """
        flag_ensure_list = False
        flag_mandatory = False
        for i_cast in casting_rule.split("|"):
            if i_cast == "ensure_list":
                flag_ensure_list = True
            if i_cast == "mandatory":
                flag_mandatory = True
            if i_cast == "optional":
                pass

        tmp_list = []
        for i_value in value:
            tmp = self._dive_next_level([i_value], children_rule, key_path)
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
                "key_path": key_path,
                "msg": "Require mandatory elements from children",
                "code": "DomParser._dive_next_level"
            })

        return tmp


    def _dive_next_level(self, xp_root_node, rules, parent_key=""):
        """
        `casting_chain`
        mandatory|optional
        """
        m = AdvancedDictDomParser()
        for xp_result_item in xp_root_node:
            for k_rule, v_rule in rules.iteritems():
                key_path = parent_key + "." + k_rule

                if k_rule.startswith("#"):  # skip commented field
                    continue

                casting_chain = v_rule[0]

                xpath_express = "|".join(i for i in v_rule[1] if not i.startswith("#")) if isinstance(v_rule[1], list)\
                else v_rule[1]

                comments = False

                if (len(v_rule) == 3 and isinstance(v_rule[2], basestring)) or len(v_rule) == 2 :
                    comments = True

                # TODO remove try/except after fix bug in checking
                try:
                    value = xp_result_item.xpath(xpath_express, namespaces = self.xpath["config.xpath.namespaces"])
                except (XPathEvalError, ) e:
                    raise DomParserException({
                        "msg": e.message,
                        "xpath": xpath_express,
                        "key_path": key_path
                    })

                if comments: # have no children nodes
                    for i_casting_chain in casting_chain.lower().split("|"):
                        error_message = ""

                        if i_casting_chain == "mandatory":
                            if not (isinstance(value, (bool, int, float, long)) or value): #! do not change (ignore bool)
                                raise DomParserException({
                                    "key_path": key_path,
                                    "msg": "Require mandatory elements from data type",
                                    "code": "DomParser._dive_next_level"
                                })
                                # else: is ok

                        elif i_casting_chain == "mandatory.skip":
                            if not value:
                                return AdvancedDictDomParser()

                        elif i_casting_chain == "optional":
                            pass

                        elif str_startswith(i_casting_chain, "text.", "int.", "float.", "bool.", "set."): # do not optimise here !
                            method_name = str_startswith(i_casting_chain, "text.", "int.", "float.", "bool.", "set.")[:-1]
                            value = getattr(InlineHandlers, method_name)(i_casting_chain, value)

                        elif i_casting_chain.startswith("^"):
                            if i_casting_chain[1:] in self.handlers:
                                value = self.handlers[i_casting_chain[1:]](value)

                            elif i_casting_chain in self.xpath["light_handlers"] or \
                                i_casting_chain in InlineHandlers._get_methods():

                                method_name = str_startswith(
                                    i_casting_chain,
                                    *InlineHandlers._get_methods()
                                )

                                if method_name:
                                    method_name = method_name[1:-1]

                                    value = getattr(InlineHandlers, method_name)(
                                        self.xpath["light_handlers"].get(i_casting_chain), value
                                    )

                                else:
                                    error_message = "unknown light handler function prefix"
                            else:
                                error_message = "unknown data type/rule from inline functions1"
                        else:
                            error_message = "unknown data type/rule from inline functions2"

                        if error_message:
                            raise DomParserException({
                                "key_path": key_path,
                                "msg": error_message,
                                "i_casting_chain": i_casting_chain,
                                "casting_chain": casting_chain,
                                "code": "DomParser._dive_next_level"
                            })

                    tmp = value

                else: # have children nodes
                    tmp = self._children_nodes(
                        casting_rule=casting_chain,
                        value=value,
                        children_rule=v_rule[2],
                        key_path=key_path
                    )

                m.dom_push(k_rule, tmp)

        return m

    def set_handlers(self, handlers):
        # TODO set generators
        self.handlers = dict([(i.__name__, i) for i in handlers])

    def _reformat(self, result):
        # TODO add more description
        a = AdvancedDictDomParser()
        for reformat in self.xpath["reformat"]:
            if "update" in reformat:
                from_, to_ = reformat["update"]
                a.update()
                result[from_].update(result[to_])
            elif "rename" in reformat:
                from_, to_ = reformat["rename"]
                result.rename_key(from_, to_)
            elif "delete" in reformat:
                for i in reformat["delete"]:
                    del result[i]

        return result

    def _dive_root_level(self, xpath_result):
        len_xp_result = len(xpath_result)

        if len(xpath_result) != 1:
            raise DomParserException({
                "msg": "Failed root detection",
                "xpath_expression": self.xpath["config.xpath.root"],
                "roots_numbers": len_xp_result
            })

        result = self._dive_next_level(xpath_result, self.xpath["rules"])

        if type(result) == list and len(result) == 1:
            result = result[0]

        result = self._reformat(result)

        return result

    def dive_xml_root_level(self, xml,  handlers = None):
        if handlers:
            self.set_handlers(handlers)

        if not self.xpath:
            self.xpath = self.get_version()

        etree_xml = None
        if isinstance(xml, basestring):
            try:
                etree_xml = etree.fromstring(xml)
            except (XMLSyntaxError, ) as e:
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
                "msg": "xml is not str or unicode or failed initialisation",
                "type_xml": type(xml),
                "val_xml": xml
            })

        xp_result = etree_xml.xpath(
            _path=self.xpath["config.xpath.root"],
            namespaces=self.xpath["config.xpath.namespaces"]
        )

        result = self._dive_root_level(xpath_result=xp_result)
        return result

    def dive_html_root_level(self, html, to_clean=False, handlers=None, disable_br=True, disable_hr=False):
        if handlers:
            self.set_handlers(handlers)

        if not self.xpath:
            self.xpath = self.get_version()

        if isinstance(html, basestring):
            if to_clean:  # TODO fix unicode corrupted conversion
                html = clean_html(html)

            if disable_br:
                html = re.sub("(?i)\s*<\s*br\s*/?\s*>\s*", "\n", html)  # TODO replace from lxml

            if disable_hr:
                html = re.sub("(?i)\s*<\s*hr\s*/?\s*>\s*", "\n", html)  # TODO replace from lxml

            try:
                xp_root = html5lib.parse(
                    html,
                    treebuilder="lxml",
                    namespaceHTMLElements=self.xpath["config"]["xpath"]["namespaces"]
                )
            except (ValueError, ) as e:
                if e.message == "All strings must be XML compatible: Unicode or ASCII, no NULL bytes or control characters":
                    xp_root = None
                    # bad_character_list = self.xpath.get("bad_character_list")
                    # if bad_character_list:
                    #     e = None
                    #
                    #     for i_replace in bad_character_list:
                    #         i_replace = i_replace.decode("unicode-escape").encode("utf-8")
                    #         html = html.replace(i_replace, "")
                    #
                    #         try:
                    #             xp_root = html5lib.parse(
                    #                 html,
                    #                 treebuilder="lxml",
                    #                 namespaceHTMLElements=self.xpath["config"]["xpath"]["namespaces"]
                    #             )
                    #             break
                    #         except ValueError, skip:
                    #             e = skip
                    #     else:
                    #         raise e

                    if not xp_root:
                        if self.debug:
                            print("[WARNING] html5lib->", e.message)
                        html = html.decode("utf-8")

                        for i_char_code in [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19,
                                18, 17, 16, 15, 14, 11, 8, 7, 6, 5, 4, 3, 2, 1]:
                            if unichr(i_char_code) in html:
                                if self.debug:
                                    print("[WARNING] remove BAD char code `%d` from html" % i_char_code)
                                html = html.replace(unichr(i_char_code), "")

                        xp_root = html5lib.parse(
                            html,
                            treebuilder="lxml",
                            namespaceHTMLElements=self.xpath["config"]["xpath"]["namespaces"]
                        )

                else:
                    raise

            xp_result = xp_root.xpath(
                _path=self.xpath["config.xpath.root"],
                namespaces=self.xpath["config.xpath.namespaces"]
            )
        else:
            xp_result = html

        result = self._dive_root_level(xp_result)

        return result