#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_linkedin_com_people_profile():
    """
    >>> test_linkedin_com_people_profile()
    constructor DOMParser
    {
        "additional": {
            "honors": "• GRE test applicant, Quantitative Section Score 760/800, Kiev October, 2009\\n• Algorithm Development, Distributed and Parallel Programming 2006\\n• Projecting & Assembling in Solid Works, Balţi Moldova 2006\\n• Trainings: Learning Experience, Leadership Challenges, Management Simulation, Team Building, AIESEC, Moldova 2006\\n• Goal Setting, Reward and Recognition, Company’s Day, AIESEC, Vadul lui Voda, Moldova 2006\\n• 3rd place in the Technical Republican Informatics Olympics, Chisinau, Moldova\\n• 3rd place in the Computer Science Municipal Contest, Balti, Moldova\\n• 2nd place in the Mathematics Olympics “Mihai Eminescu” High School, Balti, Moldova",
            "pubgroups": [
                {
                    "group_data": ".NET Developers",
                    "group_logo": "linkedin_com_people_profile_files/0658e49.png"
                },
                {
                    "group_data": ".NET People",
                    "group_logo": "linkedin_com_people_profile_files/03d7c76.png"
                },
                {
                    "group_data": "C# Developers / Architects",
                    "group_logo": "linkedin_com_people_profile_files/2436faf.png"
                },
                {
                    "group_data": "Developer & Technology Professionals",
                    "group_logo": "linkedin_com_people_profile_files/2fbe7da.png"
                },
                {
                    "group_data": "IT Recruiters",
                    "group_logo": "linkedin_com_people_profile_files/2f71da1.png"
                },
                {
                    "group_data": "Java Developers",
                    "group_logo": "linkedin_com_people_profile_files/2b66210.png"
                },
                {
                    "group_data": "Java EE Professionals",
                    "group_logo": "linkedin_com_people_profile_files/163c098.png"
                },
                {
                    "group_data": "OOP Jobs Network (OOPJN)",
                    "group_logo": "linkedin_com_people_profile_files/22bdf82.png"
                },
                {
                    "group_data": "OpenNetworker.com",
                    "group_logo": "linkedin_com_people_profile_files/2e82a36.png"
                },
                {
                    "group_data": "Software Engineering Productivity / SEPforum.net",
                    "group_logo": "linkedin_com_people_profile_files/15c1670.png"
                },
                {
                    "group_data": "The IT Developer Network",
                    "group_logo": "linkedin_com_people_profile_files/14ac3b3.png"
                },
                {
                    "group_data": "TopLinked.com (Open Networkers)",
                    "group_logo": "linkedin_com_people_profile_files/28770ed.jpg"
                }
            ],
            "websites": [
                {
                    "href": "http://www.linkedin.com/redir/redirect?url=http%3A%2F%2Fwww%2Efacebook%2Ecom%2Fpavel%2Efusu&urlhash=ofNk",
                    "name": "Facebook Profile"
                }
            ]
        },
        "education": [
            {
                "degree": "M.S",
                "major": "Computer Science",
                "name": "Maharishi University of Management",
                "period": {
                    "dtend": "2012-12-31",
                    "dtstart": "2010-01-01"
                }
            },
            {
                "degree": "B.S",
                "major": "Informational Technologies",
                "name": "Universitatea Tehnică a Moldovei",
                "period": {
                    "dtend": "2009-12-31",
                    "dtstart": "2005-01-01"
                }
            },
            {
                "degree": "High School Diploma",
                "major": "Exact Sciences",
                "name": "Liceul \\"Mihai Eminescu\\", Balti",
                "period": {
                    "dtend": "2005-12-31",
                    "dtstart": "2002-01-01"
                }
            }
        ],
        "experience": {
            "languages": [
                {
                    "lang": "English",
                    "proficiency": "(Full professional proficiency)"
                },
                {
                    "lang": "Romanian",
                    "proficiency": "(Native or bilingual proficiency)"
                },
                {
                    "lang": "Russian",
                    "proficiency": "(Native or bilingual proficiency)"
                },
                {
                    "lang": "French",
                    "proficiency": "(Limited working proficiency)"
                },
                {
                    "lang": "Spanish",
                    "proficiency": "(Elementary proficiency)"
                }
            ],
            "summary": {
                "description": "Generic & Object Oriented Programming\\nMultithreaded & Network Applications\\nSoftware Engineering & Development\\nSoftware Testing & Implementation\\nProblem Solving & Analysis\\nRequirements Gathering\\nAlgorithm Development\\nData Structure Design\\nCommunication Skills\\nProject Management\\nCustomer Relations\\nTeam Leadership\\nDesign Patterns",
                "specialties": "C/C++, C#, Java, Transact/SQL, Pascal, \\nAssembler, Visual Basic, HTML, CSS, XML, AJAX, JavaScript, JSP, JSF, \\nWSDL, PHP, ASP.NET, SQL, MS Access, MySQL, Oracle, MS Visual Studio, \\nRational Rose, C Builder, Delphi, Dreamweaver, Eclipse, NetBeans, CVS, \\nUML, Design Patterns, Networking, Internationalization, Module and \\nSystems Level Testing, Strong knowledge of the software lifecycle, \\nSolidWorks, AutoCAD, MatLab\\nSpring, Hibernate. JMS, JUNIT, CorelPaint, Flash MX, Apache, IIS 6, Maven, Web Services"
            }
        },
        "first_name": "Pavel",
        "industry": "Computer Software",
        "last_name": "Fusu",
        "locality": "Cleveland/Akron, Ohio Area",
        "overview": {
            "conn_number": 145,
            "current": [
                "Software Engineer"
            ],
            "recommend": 9
        },
        "title": "Ambitious Software Engineer"
    }
    destructor DOMParser
    """
    dpf = DomParserFile(
        name = "test",
        source = "/oknetwiki/trunk/py_lib/vsft/test/linkedin/linkedin_com_people_profile.json"
    )

    xpath = dpf.get_version()

    dpf.validate_configs(xpath)

    html = open("/oknetwiki/trunk/py_lib/vsft/test/linkedin/linkedin_com_people_profile.html").read()

    m = dpf.dive_html_root_level(html = html)

    print m.get_pretty()
