======================
Continuous Integration
======================

travis-ci.com
=============

Unfortunately travis do not support bitbucket
see https://github.com/travis-ci/travis-ci/issues/667

magnum-ci.com
=============

Dependencies installation:
--------------------------

sudo apt-get -y update
sudo apt-get install -y python-pip libxml2-dev libxslt1-dev python-dev cython zlib1g-dev
sudo pip install --upgrade setuptools
sudo pip install --upgrade pip
sudo pip install -r requirements-pip-dev.txt

Test suite commands:
--------------------

python setup.py test
