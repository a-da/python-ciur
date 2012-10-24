def test_manta_com_city():
    """
    >>> test_manta_com_city()
    constructor DOMParser
    {
        "paths": [
            {
                "path": "/world/Europe/Moldova/-/Balti/"
            },
            {
                "path": "/world/Europe/Moldova/-/Basarabeasca/"
            },
            {
                "path": "/world/Europe/Moldova/-/Bender/"
            },
            {
                "path": "/world/Europe/Moldova/-/Bendery/"
            },
            {
                "path": "/world/Europe/Moldova/-/Bulboaca/"
            },
            {
                "path": "/world/Europe/Moldova/-/Cahul/"
            },
            {
                "path": "/world/Europe/Moldova/-/Calaras/"
            },
            {
                "path": "/world/Europe/Moldova/-/Calarasi/"
            },
            {
                "path": "/world/Europe/Moldova/-/Caragas/"
            },
            {
                "path": "/world/Europe/Moldova/-/Caragasi+Village/"
            },
            {
                "path": "/world/Europe/Moldova/-/Causeni/"
            },
            {
                "path": "/world/Europe/Moldova/-/Causeni+Orasul/"
            },
            {
                "path": "/world/Europe/Moldova/-/Ceadir+Lunga/"
            },
            {
                "path": "/world/Europe/Moldova/-/Ceadir&%252308211%253BLunga/"
            },
            {
                "path": "/world/Europe/Moldova/-/Ceadir-Lunga/"
            },
            {
                "path": "/world/Europe/Moldova/-/Cedir+-+Lunga/"
            },
            {
                "path": "/world/Europe/Moldova/-/Chirca/"
            },
            {
                "path": "/world/Europe/Moldova/-/Chishinau/"
            },
            {
                "path": "/world/Europe/Moldova/-/Chisianu/"
            },
            {
                "path": "/world/Europe/Moldova/-/Chisinau/"
            },
            {
                "path": "/world/Europe/Moldova/-/Chisnau/"
            },
            {
                "path": "/world/Europe/Moldova/-/Cimislia/"
            },
            {
                "path": "/world/Europe/Moldova/-/Com+Lozova/"
            },
            {
                "path": "/world/Europe/Moldova/-/Comrat/"
            },
            {
                "path": "/world/Europe/Moldova/-/Cosnita/"
            },
            {
                "path": "/world/Europe/Moldova/-/Criuleni/"
            },
            {
                "path": "/world/Europe/Moldova/-/Drochia/"
            },
            {
                "path": "/world/Europe/Moldova/-/Falesti/"
            },
            {
                "path": "/world/Europe/Moldova/-/Floresti/"
            },
            {
                "path": "/world/Europe/Moldova/-/Grigoriopol/"
            },
            {
                "path": "/world/Europe/Moldova/-/Hincesti/"
            },
            {
                "path": "/world/Europe/Moldova/-/Ialoveni/"
            },
            {
                "path": "/world/Europe/Moldova/-/Karagash/"
            },
            {
                "path": "/world/Europe/Moldova/-/Kishinev/"
            },
            {
                "path": "/world/Europe/Moldova/-/Leova/"
            },
            {
                "path": "/world/Europe/Moldova/-/Lozova+Stul/"
            },
            {
                "path": "/world/Europe/Moldova/-/Nisporeni/"
            },
            {
                "path": "/world/Europe/Moldova/-/Orhei/"
            },
            {
                "path": "/world/Europe/Moldova/-/Pljevlja/"
            },
            {
                "path": "/world/Europe/Moldova/-/Rezina/"
            },
            {
                "path": "/world/Europe/Moldova/-/Ribnita/"
            },
            {
                "path": "/world/Europe/Moldova/-/Rybnitsa/"
            },
            {
                "path": "/world/Europe/Moldova/-/Sadova/"
            },
            {
                "path": "/world/Europe/Moldova/-/Sanatauca/"
            },
            {
                "path": "/world/Europe/Moldova/-/Satul+Vadul-Rascov/"
            },
            {
                "path": "/world/Europe/Moldova/-/Soroca/"
            },
            {
                "path": "/world/Europe/Moldova/-/Straseni/"
            },
            {
                "path": "/world/Europe/Moldova/-/Straseni+City/"
            },
            {
                "path": "/world/Europe/Moldova/-/Talmaza/"
            },
            {
                "path": "/world/Europe/Moldova/-/Taraclia/"
            },
            {
                "path": "/world/Europe/Moldova/-/Test+Town/"
            },
            {
                "path": "/world/Europe/Moldova/-/Tiraspol/"
            },
            {
                "path": "/world/Europe/Moldova/-/Tohatin/"
            },
            {
                "path": "/world/Europe/Moldova/-/Truseni/"
            },
            {
                "path": "/world/Europe/Moldova/-/Tuzara/"
            },
            {
                "path": "/world/Europe/Moldova/-/Ugheni/"
            },
            {
                "path": "/world/Europe/Moldova/-/Ungheni/"
            },
            {
                "path": "/world/Europe/Moldova/-/Vadul+Lui+Voda/"
            },
            {
                "path": "/world/Europe/Moldova/-/Varnita/"
            },
            {
                "path": "/world/Europe/Moldova/-/Vasieni/"
            }
        ]
    }
    destructor DOMParser
    """
    dpf = DomParserFile(
        name = "test",
        source = "/oknetwiki/trunk/py_lib/vsft/test/manta_com_city.json"
    )

    xpath = dpf.get_version()

    dpf.validate_configs(xpath)

    html = open("/oknetwiki/trunk/py_lib/vsft/test/manta_com_city.html").read()

    m = dpf.dive_html_root_level(html = html)

    print m.get_pretty()

