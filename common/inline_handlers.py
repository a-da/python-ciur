import datetime
import decimal
import re
import json

from HTMLParser import HTMLParser
from lxml.etree import _Element
from lxml.etree import _ElementStringResult, _ElementUnicodeResult
from lxml.etree import tostring

from ciur.common import JsonException


class InlineHandlersException(JsonException):
    pass


class HttpRaiseException(JsonException):
    """
    raise http error if found some match in html
    http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
    """
    pass


class InlineHandlers(object):
    rec_round = re.compile("round_(\d)")
    html_parser = HTMLParser()

    @staticmethod
    def int(casting_rule, value):
        # TODO casting_rule
        # TODO int.positive
        # TODO int.negative
        # TODO int.non_positive
        # TODO int.non_negative
        """
        convert into int
        """

        if isinstance(value, list):
            value = [i for i in value if not (isinstance(i, _Element) and i.text == None)] # do not optimise

        if not value: # None
            return value


        if isinstance(value, (float, long, int, basestring, bool)):
            try:
                value = int(value)
                return value
            except ValueError, e:
                raise InlineHandlersException({
                    "msg": e.message,
                    "suggestion": "tried to make convert for only one item and expected to be int",
                    "code": "InlineHandlers.int"
                })

        v_len = len(value)

        if not v_len:
            return None

        tmp_value = []
        for i_value in value:
            if isinstance(i_value, _Element):
                i_value = i_value.text
            try:
                i_value = int(i_value, 0)
            except ValueError, e:
                if e.message.startswith("invalid literal for int() with base 0:"):
                    raise InlineHandlersException({
                        "msg": e.message,
                        "suggestion": "tried to make convert for more than one item and expected to be int",
                        "code": "InlineHandlers.int",
                        "i_value": i_value
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


    @classmethod
    def float(cls, casting_rule, value):
        # TODO casting_rule
        # TODO float.positive
        # TODO float.negative
        # TODO float.non_positive
        # TODO float.non_negative
        """
        casting into float
        """

        if isinstance(value, list):
            value = [i for i in value if not (isinstance(i, _Element) and i.text == None)] # do not optimise

        if not value: # None
            return value

        if isinstance(value, (float, long, int, basestring, bool)):
            value = float(decimal.Decimal(value))
            return value

        v_len = len(value)
        if not v_len:
            return None

        if v_len > 1:
            raise InlineHandlersException({
                "msg": "undesired behavior, xpath int should have only one item but have `%d` items" % v_len,
                "code": "InlineHandlers._float"
            })

        casting_rule = casting_rule[len("float."):]
        value = value[0]
        value = value.text

        if casting_rule == "has_comma_sep":
            if "." in value:
                raise InlineHandlersException({
                    "msg": "^float.has_comma_sep expect to have comma separator instead of dot separator",
                    "suggestion": "review/update jxpath rules",
                    "got": value
                })
            value = value.replace(",", ".")


        try:
            value = decimal.Decimal(value)
            value = float(value)
        except decimal.InvalidOperation, e:
            raise InlineHandlersException({
                "msg": e.message,
                "suggestion": "failed float casting",
                "code": "InlineHandlers.float"
            })

        m = cls.rec_round.search(casting_rule)
        if m:
            value = round(value, int(m.group(1)))

        return value


    @staticmethod
    def bool(casting_rule, value):
        # TODO casting_rule
        """
        casting into int
        """

        if isinstance(value, list):
            value = [i for i in value if not (isinstance(i, _Element) and i.text == None)] # do not optimise

        if not value and not isinstance(value, (float, int, long, bool)):
            return False


        if isinstance(value, (float, long, int, bool)):
            value = bool(value)
            return value

        elif isinstance(value, basestring):
            value = value.strip()
            if value.lower() == "false" or value == "":
                return False
            return True

        v_len = len(value)
        if not v_len:
            return None

        if v_len > 1:
            raise InlineHandlersException({
                "msg": "undesired behavior, xpath bool should have only one item but have `%d` items" % v_len,
                "code": "InlineHandlers.bool"
            })

        value = value[0]
        if not isinstance(value, _ElementStringResult):
            value = value.text

        if value.lower() == "false":
            return False

        return True


    @staticmethod
    def set(casting_rule, value):

        if isinstance(value, list):
            value = [i for i in value if not (isinstance(i, _Element) and i.text == None)]  # do not optimise
            value = [i for i in value if i]  # remove null elements

        if not value:  # None
            return value

        return list(set(value))

    @classmethod
    def text(cls, casting_rule, value):
        # TODO add doctest
        # TODO text.lower
        # TODO text.upper
        # TODO text.capitalize
        # TODO text.title
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
        flag_force_list = False
        flag_do_not_strip = False
        flag_join_by_space = False
        flag_join_by_new_line = False
        flag_tail = False
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

        value_list = []
        for i_value in value:
            if isinstance(i_value, (float, long, int, bool)):
                i_value = str(i_value)

            else:
                if not isinstance(i_value, basestring):
                    if flag_tail:
                        i_value = i_value.tail
                    else:
                        i_value = i_value.text
                        if not i_value:
                            continue

                if i_value and not isinstance(i_value, basestring):
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
            if isinstance(value[length], basestring):
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


    @staticmethod
    def default(rule, value):
        """
        set default value
        """
        def _f(v):
            if not v:
                if isinstance(v, (int, bool, float, long)):
                    return v
                else:
                    return rule
            return v

        if not value:
            return rule

        if isinstance(value, list):
            value = map(_f, value)

        else:  # str
            value = _f(value)

        return value


    @staticmethod
    def xml(rule, value):
        """
        handle `xml` inline function declarations from jxpath
        """
        def _f(v):
            v = tostring(v, method="html", pretty_print=rule.get("pretty_print"))
            return v

        if isinstance(value, list):
            value = map(_f, value)

        else:  # str
            value = _f(value)

        return value


    @classmethod
    def html(cls, rule, value):
        """
        handle `html` inline function declarations from jxpath
        """
        res = cls.xml(rule, value)

        def _f(v):
            v = v.replace(' xmlns:html=\"http://www.w3.org/1999/xhtml\">', ">")
            v = v.replace(' xmlns:html=\"http://www.w3.org/1999/xhtml\" ', " ")
            v = v.replace("<html:", "<")
            v = v.replace("</html:", "</")
            return v

        if type(res) == list:
            res = map(_f, res)
            if len(res) == 1:
                return res[0]
        else:
            res = _f(res)

        return res


    @classmethod
    def inner_html(cls, rule, value):
        """
        handle `inner_html` inline function declarations from jxpath
        return inner markup-ed content from html
        """
        value = cls.html(rule, value)
        if isinstance(value, list):
            value = map(cls._extract_content_tags, value)
            if len(value) == 1:
                return value[0]
        else:
            value = cls._extract_content_tags(value)

        return value


    @staticmethod
    def _strip_tag_block(block):
        """
        inner function for _extract_content_tags
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
    def _extract_content_tags(cls, block):
        #print "---0", block

        #TODO doctest
        """
        inner function for _inner_html_by_light_handlers
        """
        beg_tag = re.compile("^<\s*([^>]+?)( +[^>]+)?\s*>\s*")
        end_tag = re.compile("\s*<\s*/([^>]+)\s*>\s*$")
        block = cls._strip_tag_block(block)

        # -[2]- extract tags
        m = beg_tag.search(block)
        if m:
            open_tag = m.group(1)
        else:
            raise InlineHandlersException({
                "msg": "can't find open tag",
                "tags_block": block
            })

        m = end_tag.search(block)
        if m:
            close_tag = m.group(1)
        else:
            raise InlineHandlersException({
                "msg": "can't find close tag",
                "tags_block": block
            })

        if open_tag != close_tag:
            raise InlineHandlersException({
                "msg": "open and close tag are different",
                "tags_block": block,
                "open_tag": open_tag,
                "close_tag": close_tag
            })

        #print "0---", open_tag
        #print "1---", close_tag

        block = beg_tag.sub("", block)
        #print "a---", repr(block)
        block = end_tag.sub("", block)
        #print "b---", repr(block)


        #print "---1", block
        return block


    @staticmethod
    def replace(rule, value):
        """
        handle `replace` inline function declarations from jxpath
        do replace in text based on string and regular expressions
        """
        def _f(v):
            for i_replace in rule:
                v = v.strip()
                if not v: break
                counts = i_replace.get("counts", 1)
                while counts:
                    counts -= 1
                    to_ = i_replace["to"]

                    if "from_str" in i_replace:
                        v = v.replace(i_replace["from_str"], to_)

                    elif "from_re" in i_replace:
                        v = i_replace["from_re"].sub(to_, v)

                    else:
                        raise InlineHandlersException({
                            "msg": "can't detected replace key `from`",
                            "keys": i_replace,
                            "expected": ["from_re", "from_str"]
                        })
            return v

        if not value:
            pass  # skip

        elif isinstance(value, list):
            value = map(_f, value)

        else:  # str
            value = _f(value)

        return value


    @staticmethod
    def drain(rule, value):
        # TODO write doctests
        """
        handle `drain` inline function declarations from jxpath
        extract string (drain) from text using regular expression
        """
        def _f(v):
            v = v.strip()
            m = rule["re"].search(v)
            if not m:
                return None

            v = m.group(rule["group"])
            return v

        if not value:
            pass # skip

        elif isinstance(value, list):
            value = map(_f, value)

        else: #str
            value = _f(value)

        return value

    @staticmethod
    def json(rule, value):
        # TODO write doctests
        """
        TODO write doc
        >>> InlineHandlers.json("", '{"a": 123}')
        {u'a': 123}
        >>> InlineHandlers.json("", '{"a": "/profile/profile\\u002dv2\\u002dpymk"}')
        {u'a': u'/profile/profile-v2-pymk'}
        """
        if not value:
            pass  # skip

        elif isinstance(value, list):
            value = map(unicode, value)
            value = map(json.loads, value)

        else:  # str
            #print repr(value)
            #value = unicode(value)
            value = json.loads(value)

        return value

    @staticmethod
    def lower(rule, value):
        # TODO write doctests
        """
        """
        if not value:
            pass  # skip

        elif isinstance(value, list):
            value = [i.lower() for i in value]

        else:
            value = value.lower()

        return value

    @staticmethod
    def upper(rule, value):
        # TODO write doctests
        """
        """
        if not value:
            pass  # skip

        elif isinstance(value, list):
            value = [i.upper() for i in value]

        else:
            value = value.upper()

        return value

    @staticmethod
    def http_raise(rule, value):
        if value:
            raise HttpRaiseException({
                "msg": "found http error match",
                "status_code": rule["status_code"],
                "message": rule["message"],
                "value": value
            })
        return value

    @staticmethod
    def date(rule, value):
        # TODO write doctests
        """
        handle `date` inline function declarations from jxpath
        convert date from string into datetime
        """
        def _f(v):
            exception_ = None
            for i_date in rule:
                try:
                    v = datetime.datetime.strptime(v, i_date)
                except ValueError, e:
                    exception_ = e
                else:
                    return v

            raise InlineHandlersException({
                "msg": "cant convert time",
                "exc": str(exception_)
            })

        if not value:
            pass  # skip

        elif isinstance(value, list):
            value = map(_f, value)

        else:  # str
            value = _f(value)

        return value


    @staticmethod
    def hash_map(rule, value):
        # TODO multiply key sub-items by separators
        """
        get map equivalent for string items
        """
        def _f(v):
            if not isinstance(v, basestring):
                raise InlineHandlersException({
                    "msg": "expected only string or unicode format",
                    "got": repr(v)
                })

            map_ = rule["map"]

            if v in map_:
                return map_[v]

            else:
                # check in key name by separators
                # remove after implement TODO
                operator = rule.get("operator")
                sep = rule["separator"]
                if operator not in ("in", "startswith", "endswith"):
                    raise InlineHandlersException({
                        "msg": "expected hash_map.operator in [in, startswith, endswith]",
                        "got": repr(operator)
                    })

                if operator == "in":
                    for k_map in map_:
                        if v in k_map.split(sep):
                            return map_[k_map]

                elif operator == "startswith":
                    for k_map in map_:
                        for i_split in k_map.split(sep):
                            if v.startswith(i_split):
                                return map_[k_map]

                elif operator == "endswith":
                    for  k_map in map_:
                        for i_split in k_map.split(sep):
                            if v.endswith(i_split):
                                return map_[k_map]

                default = rule["default"]
                if not default:
                    return v
                else:
                    return default

        if not value:
            pass  # skip

        elif isinstance(value, list):
            value = map(_f, value)

        else:  # str
            value = _f(value)

        return value

    @classmethod
    def _get_methods(cls):
        return ["^%s:" % i for i in cls.__dict__.keys() if not i.startswith("_")]