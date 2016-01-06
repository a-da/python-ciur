==================
Info for developer
==================

Code Check list::
=================

   * from time to time check PyUnusedLocal
   * run all tests:
        1. prepare test (optional)

            rm tests/.coverage.ciur # coverage cash file

        2. setup.py test
        3. check test cover tests/html-cov-ciur/index.html


   * check code smell:

        setup.py lint

   * TODO run documentation build

        setup.py sphinx


IDE pycharm tuning::
====================

Appearance & Behavior > Appearance

    Theme: Darcula

Editor > Code Style

    Right margin (columns): 80

Editor > Spelling > [TAB] Dictionaries

    Custom Dictionaries Folder: ${CIUR_HOME}


Editor > General > Appearance

    Show line numbers (on)

    Show whitespaces:
       - Leading (off)
       - Inner (off)
       - Trailing (on)


Project: ciur > Project Interpreter

    Project Interpreter: </opt/python-env/ciur/bin/python>

Project: ciur > Project Dependencies (in case if you want do dig in one of
    ciur.example.* projects)

    select ``ciur.example.<project_name>`` and check ``ciur``

Tools > Python Integrated Tools

    Package requirements file: ${CIUR_HOME}/requirements-pip-dev.txt


TODO: Other IDE tuning::
========================

    Add here tuning eclipse, sublime ...
    Read contribution protocol link <link> before !

