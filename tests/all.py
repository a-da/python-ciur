import nose
import sys

sys.argv = sys.argv[0:]

sys.argv += """\
--all-modules
--traverse-namespace
--with-coverage
--cover-tests
--with-doctest
../ciur\
""".split("\n")


nose.run_exit()

sys.argv = sys.argv[0:]

sys.argv += """\
--all-modules
--traverse-namespace
--with-coverage
--cover-tests
--with-doctest
../ciur\
""".split("\n")


nose.run_exit()
