check your version of python, we expect 3.6::

    python3 --version
    Python 3.5.2

In my case is not 3.6 And I need to follow instruction from
https://bitbucket.org/snippets/ada/Aq8o9B/set-up-python-virtual-environment#file-compile_python_3_6.rst

Create python virtual environment `/opt/python-ciur-web-sever-tornado` follow link from above

Intall pipenv (see https://github.com/pypa/pipfile)::

    /opt/python-ciur-web-sever-tornado/bin/pip install pipenv

Install dependencies from `Pipfile`

    cd /path/to/Pipfile
    . /opt/python-ciur-web-sever-tornado/bin/activate
    pipenv install .
