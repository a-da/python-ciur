
Code Check list::
   * from time to time check PyUnusedLocal
   * run all tests:
        1. prepare test (optional)

            rm tests/.coverage.ciur # coverage cash file

        2. setup.py test
        3. check test cover tests/html-cov-ciur/index.html


   * check code smell:
        setup.py lint
