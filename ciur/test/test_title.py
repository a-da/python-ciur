"""
>>> html = '''<html>
... <body><h1><title> Some title h1</title></h1><h2><title> Some title h2</title></h2></body>
... </html>
... '''
>>> import ciur.wrapper
>>> xp_json = '''{
...     "versions": [{
...         "config" : { "xpath" : { "root": "/html/body"}},
...         "rules": {
...             "title": ["text.|mandatory", ".//title"]
...         },
...         "light_handlers": {}
...     }]
... }'''
>>> print ciur.wrapper.parse(html, xp_json, "html")
{"title": ["Some title h1", "Some title h2"]}
"""