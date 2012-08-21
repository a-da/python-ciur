def test_manta_com_pagination():
    """
    >>> test_manta_com_pagination()
    constructor DOMParser
    {
        "paths": [
            {
                "path": "http://www.manta.com/coms2/dnbcompany_..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_wqsdl2"
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_wqqwg1"
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_wqv30..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_wqt3..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_wqv3..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_wqqwh4"
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_wqv3..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_wqs0..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_wqts3..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_wqv30..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_..."
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_wqt9y3"
            },
            {
                "path": "http://www.manta.com/coms2/dnbcompany_..."
            }
        ]
    }
    destructor DOMParser
    """
    dpf = DomParserFile(
        name = "test",
        source = "/oknetwiki/trunk/py_lib/vsft/test/manta_com_pagination.json"
    )
    xpath = dpf.get_version()

    def fun_lol(value):
        return [value]
    dpf.set_handlers([fun_lol])
    dpf.validate_configs(xpath)


    html = open("/oknetwiki/trunk/py_lib/vsft/test/manta_com_pagination.html").read()

    m = dpf.dive_html_root_level(html = html, handlers=[fun_lol])

    print m.get_pretty()
