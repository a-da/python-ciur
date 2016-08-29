Testing string_join xpath function
==================================
>>> import os

>>> from ciur import parse, pretty_json
>>> from ciur.rule import Rule
>>> from ciur.bnf_parser import external2dict

>>> html_document = parse.Document("""<html>
... <body>
... <div class="paragraph">
...     <p>Do you want to face a new challenge?</p>
...     <p>Building a platform with top-notch</p>
... </div>
... </body>
... </html>""")

>>> string_join_sample_rule1 = Rule.from_dsl("""
... text `//body/div[@class='paragraph']//text()` +
... """)[0]

>>> data = parse.html_type(html_document, string_join_sample_rule1)
>>> print pretty_json(data)  # doctest: +NORMALIZE_WHITESPACE
{
    "text": [
        "\n    ",
        "Do you want to face a new challenge?",
        "\n    ",
        "Building a platform with top-notch",
        "\n"
    ]
}

>>> string_join_sample_rule2 = Rule.from_dsl("""
... text `//body/div[@class='paragraph']//text()` string_join +
... """)[0]

>>> data = parse.html_type(html_document, string_join_sample_rule2)
>>> print pretty_json(data)  # doctest: +NORMALIZE_WHITESPACE
{
    "text": "\n    Do you want to face a new challenge?\n    Building a platform with top-notch\n"
}

>>> string_join_sample_rule3 = Rule.from_dsl("""
... text `//body/div[@class='paragraph']//text()` string_join('|') +
... """)[0]

>>> data = parse.html_type(html_document, string_join_sample_rule3)
>>> print pretty_json(data)  # doctest: +NORMALIZE_WHITESPACE
{
    "text": "\n    |Do you want to face a new challenge?|\n    |Building a platform with top-notch|\n"
}
