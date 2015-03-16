import json
from ciur.common.dom_parser_object_json import DomParserObjectJson

from ciur.common.dom_parser_str_json import DomParserStrJson
from ciur.common.dom_parser_file import DomParserFile


def parse(data, xp_json, page_type):
    if isinstance(data, file):
        data = data.read()

    if isinstance(xp_json, file):
        xp_json = json.load(xp_json)

    if not isinstance(data, str):
        raise NotImplemented

    if isinstance(xp_json, dict):
        dom_parser_file = DomParserObjectJson(xp_json)
    elif "{" not in xp_json:
        dom_parser_file = DomParserFile(xp_json)
    else:
        dom_parser_file = DomParserStrJson(xp_json)

    # TODO add warning in logs for file not found

    dom_parser_file.validate_configs(dom_parser_file.get_version(), strict=False)

    if page_type == "html":
        res = dom_parser_file.dive_html_root_level(data)
    elif page_type == "xml":
        res = dom_parser_file.dive_xml_root_level(data)
    else:
        raise NotImplemented(page_type)

    return res