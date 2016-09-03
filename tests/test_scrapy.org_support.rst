Testing http://scrapy.org/companies/
====================================

>>> from ciur import parse, pretty_json
>>> from ciur.rule import Rule

>>> html_page = parse.Document("""<html><body>
... <div class="companies-container">
...     <div class="company-box">
...       <a href="http://scrapinghub.com/?_ga=1.262811468.1789615425.1471746235">
...       <img src="../img/shub-logo.png">
...       </a>
...       <span class="highlight">Scrapinghub:</span>
...     </div>
...
...     <div class="company-box">
...       <a href="http://parsely.com/"><img src="../img/01-parsely-logo.png"></a>
...       <span class="highlight">Parsely:</span>
...     </div>
...
...     <div class="company-box">
...       <a href="http://directemployersfoundation.org/">
...       <img src="../img/02-direct-employers-logo.png">
...       </a>
...       <span class="highlight">DirectEmployers Foundation:</span>
...     </div>
... </div>
... </body></html>
... """)

test internal dsl
-----------------

>>> rule = Rule("company_list", ".//div[@class='company-box']", "+",
...             Rule("name", ".//span[@class='highlight']/text()", ["+"]),
...             Rule("company_url", "./a/@href", ["+1"]),
...             Rule("blog_url", "./p/a/@href", ["*"]),
...             Rule("logo", "./a/img/@src", ["+"])
...            )

>>> data = parse.html_type(html_page, rule)
>>> print(pretty_json(data))  # doctest: +NORMALIZE_WHITESPACE
    {
        "company_list": [
            {
                "name": "Scrapinghub:",
                "company_url": "http://scrapinghub.com/?_ga=1.262811468.1789615425.1471746235",
                "logo": "../img/shub-logo.png"
            },
            {
                "name": "Parsely:",
                "company_url": "http://parsely.com/",
                "logo": "../img/01-parsely-logo.png"
            },
            {
                "name": "DirectEmployers Foundation:",
                "company_url": "http://directemployersfoundation.org/",
                "logo": "../img/02-direct-employers-logo.png"
            }
        ]
    }
