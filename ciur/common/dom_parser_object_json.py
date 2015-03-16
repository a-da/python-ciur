from advanced_types.advanced_ordered_dict import AdvancedOrderedDict
from ciur.common import DomParser


class DomParserObjectJson(DomParser):
    """
    Json object implimentation of DomParser
    1. Got xjson json object
    2. Got page string
    3. return desired data form parsed page into json format
    """
    def __init__(self, source_object, name="default name", debug=False):
        self.abstract = False
        DomParser.__init__(self, name, "from object", debug)

        self.context = AdvancedOrderedDict(source_object)

        if not self.context:  # create new one
            self.context = {
                "name": self.name,
                "version": 0,
                "versions": []
            }

    def save(self, js):
        raise NotImplemented
