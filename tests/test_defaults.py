from ciur import parse
from ciur.rule import Rule


def test_size():
    html_document = parse.Document("""<html>
    <body>
    <div class="paragraph">
        <p>Do you want to face a new challenge?</p>
        <p>Building a platform with top-notch</p>
    </div>
    </body>
    </html>
    """)
    
    rule_definition = "\n".join((
        "",
        "body `//body` +1",
        "    no_explicit_size_plus `./div[@class='paragraph']//text()` +",
        "    no_explicit_size_asterix `./div[@class='paragraph']//text()` *",
        "    none `./div[@class='none']//text()` *",
        ""))
    
    rule = Rule.from_dsl(rule_definition)[0]

    result = parse.html_type(html_document, rule)
    
    assert len(result['body']['no_explicit_size_plus']) == 5
    assert len(result['body']['no_explicit_size_asterix']) == 5
    assert result['body'].get('none') is None
   
