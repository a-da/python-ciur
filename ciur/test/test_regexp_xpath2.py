"""
>>> from __future__ import unicode_literals
>>> import ciur.some_lib.function_name_spaces
>>> import ciur.wrapper

>>> ciur.some_lib.function_name_spaces.load()

>>> html = '''<html>
... <body>
... <table cellspacing="1" cellpadding="1" border="0">
... <tbody>
...     <tr class="blue_td"><td>ISO(code)</td><td>Rate</td></tr>
...     <tr class="gray_td"><td><span>USD</span><em>1</em></td><td>479.59</td></tr>
...     <tr class="gray_td_light"><td><span>GBP</span><em>1</em></td><td>729.12</td></tr>
...     <tr class="gray_td"><td><span>AUD</span><em>1</em></td><td>374.32</td></tr>
...     <tr class="gray_td_light"><td><span>ARS</span><em>1</em></td><td>54.80</td></tr>
...     <tr class="gray_td"><td><span>DKK</span><em>1</em></td><td>70.60</td></tr>
...     <tr class="gray_td_light"><td><span>EGP</span><em>1</em></td><td>63.28</td></tr>
...     <tr class="gray_td"><td><span>EUR</span><em>1</em></td><td>526.06</td></tr>
...     <tr class="gray_td_light"><td><span>SDR</span><em>1</em></td><td>670.14</td></tr>
...     <tr class="gray_td"><td><span>TRY</span><em>1</em></td><td>184.11</td></tr>
...     <tr class="gray_td_light"><td><span>IRR</span><em>100</em></td><td>1.73</td></tr>
...     <tr class="gray_td"><td><span>ILS</span><em>1</em></td><td>119.70</td></tr>
...     <tr class="gray_td_light"><td><span>PLN</span><em>1</em></td><td>127.44</td></tr>
...     <tr class="gray_td"><td><span>LBP</span><em>100</em></td><td>31.70</td></tr>
...     <tr class="gray_td_light"><td><span>CAD</span><em>1</em></td><td>384.26</td></tr>
...     <tr class="gray_td"><td><span>INR</span><em>1</em></td><td>7.71</td></tr>
...     </tbody></table>
... </body>
... </html>
... '''

>>> xp_json = '''{
...     "versions": [{
...         "config" : { "xpath" : { "root": "/html/body"}},
...         "rules" : {
...                "items" : ["mandatory", "./table//td/span[xp2f:regexp(text(), '^[A-Z]{3}$')]/../..", {
...                    "currency": ["text.|mandatory", "./td[1]/span"],
...                    "rate": ["int.|mandatory", "./td[1]/em"],
...                    "value": ["float.|mandatory", "./td[2]"],
...                    "sell": ["float.|mandatory", "./td[2]"],
...                    "buy": ["float.|mandatory", "./td[2]"]
...                }]
...        },
...        "light_handlers": {}
...     }]
... }'''

>>> print ciur.wrapper.parse(html, xp_json, "html")  # doctest: +NORMALIZE_WHITESPACE
{"items":
[{"buy": 479.59, "currency": "USD", "rate": 1, "sell": 479.59, "value": 479.59},
{"buy": 729.12, "currency": "GBP", "rate": 1, "sell": 729.12, "value": 729.12},
{"buy": 374.32, "currency": "AUD", "rate": 1, "sell": 374.32, "value": 374.32},
{"buy": 54.8, "currency": "ARS", "rate": 1, "sell": 54.8, "value": 54.8},
{"buy": 70.6, "currency": "DKK", "rate": 1, "sell": 70.6, "value": 70.6},
{"buy": 63.28, "currency": "EGP", "rate": 1, "sell": 63.28, "value": 63.28},
{"buy": 526.06, "currency": "EUR", "rate": 1, "sell": 526.06, "value": 526.06},
{"buy": 670.14, "currency": "SDR", "rate": 1, "sell": 670.14, "value": 670.14},
{"buy": 184.11, "currency": "TRY", "rate": 1, "sell": 184.11, "value": 184.11},
{"buy": 1.73, "currency": "IRR", "rate": 100, "sell": 1.73, "value": 1.73},
{"buy": 119.7, "currency": "ILS", "rate": 1, "sell": 119.7, "value": 119.7},
{"buy": 127.44, "currency": "PLN", "rate": 1, "sell": 127.44, "value": 127.44},
{"buy": 31.7, "currency": "LBP", "rate": 100, "sell": 31.7, "value": 31.7},
{"buy": 384.26, "currency": "CAD", "rate": 1, "sell": 384.26, "value": 384.26},
{"buy": 7.71, "currency": "INR", "rate": 1, "sell": 7.71, "value": 7.71}]}
"""