import unittest

from ciur.common import DomParserFile
from ciur.common.inline_handlers import HttpRaiseException

html = """
<html>
    <head>
        <title>justin bieber spits on fans</title>
    </head>
    <body>
        <h1>Justin Bieber did not spit on fans over balcony in Toronto, says rep</h1>
        <h2 itemprop="alternativeHeadline" class="story-subheader">
            A rep for the 19-year-old singer has denied that Bieber was
            spitting on his fans below his hotel room last week, says the photos were 'superimposed.'
        </h2>
    </body>
</html>
"""

class Test(unittest.TestCase):
    def test_en(self):
        dpf = DomParserFile("../xjsons/raise_error_en.json")
        xpath = dpf.get_version()
        dpf.validate_configs(xpath)

        html = open("../html/JustinBieber_en.html").read()

        # print html
        try:
            m = dpf.dive_html_root_level(html=html)
        except HttpRaiseException, e:
            self.assertEqual(e.value["message"], 'Justin Bieber Must Die')


    def test_en2(self):
        dpf = DomParserFile("../xjsons/raise_error_en2.json")
        xpath = dpf.get_version()
        dpf.validate_configs(xpath)

        html = open("../html/JustinBieber_en.html").read()

        m = dpf.dive_html_root_level(html=html)

        self.assertEqual(m, {})

    def test_ru(self):
        dpf = DomParserFile("../xjsons/raise_error_ru.json")
        xpath = dpf.get_version()
        dpf.validate_configs(xpath)

        html = open("../html/JustinBieber_ru.html").read()

        try:
            m = dpf.dive_html_root_level(html=html)
        except HttpRaiseException, e:
            self.assertEqual(e.value["message"], 'Justin Bieber Must Die')


if __name__ == '__main__':
    unittest.main(verbosity=2)