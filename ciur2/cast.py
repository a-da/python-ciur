from lxml.etree import _ElementStringResult


def str_(value, *args):
    if isinstance(value, str):
        return value

    return value.text


def size_(got, mandatory_or_optional, expect):
    if mandatory_or_optional == "mandatory" and not got:
        assert False, "expect mandatory 1"

    if expect:
        assert got, "expect mandatory 2"

    if expect:
        assert got == expect, "expect size `%s`, got `%s`" % (expect, got)
