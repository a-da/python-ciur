Stuff related to testing
========================

Command line testing
--------------------

tests/run.py -- run all tests


IDE tests
---------

CLI is a power but for developing most of time IDE is better

PYCHARM
+++++++

Unfortunately pycharm is stupid in term of testing feature.
It do not allow to make implicit (select/create 2 clicks) py.tests

We should (at the moment pycharm 5.0) make all test runner explicit.

follow: Menu -> Run -> Edit Configuration -> + -> Python tests -> py.test:

    * run doctest from source folder

        Name: py.test in ciur
        Configuration:
            py.tests:
                Target: ./ciur

    * run all posible test from test folder

        Name: py.test in tests
        Configuration:
            py.tests:
                Target: .

            Environment:
                Working directory: ./tests




ECLIPSE
+++++++

TODO: add description how to run this test in case there are some interest in ECLIPSE or other python related IDE



