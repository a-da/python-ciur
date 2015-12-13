
Code Check list::
   * from time to time check PyUnusedLocal
   * run all tests:
        1. setup.py test --addopts=ciur
        2. setup.py test --addopts=tests
        3. check test cover tests/html-cov-ciur/index.html

   * check code smell:
        setup.py lint
