==========================
Python virtual environment
==========================

We will use only python version 3.5

Compile python it from source code
----------------------------------

In case you don not have it, follow bellow instructions to compile it from source code.

.. code-block:: bash

    #!/bin/bash
    # script: compile_python

    PYTHON_VERSION=3.6.1

    cd /opt
    wget --version > /dev/null || apt-get install -y wget # install wget in case is not present
    wget -c "https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz"

    xz --version || apt-get install -y xz-utils  # install xz in case is not present
    tar xf Python-${PYTHON_VERSION}.tar.xz
    cd Python-${PYTHON_VERSION}/

    gcc --version > /dev/null || apt-get install -y build-essential  # install xz in case is not present
    apt-get install -y libssl-dev # ssl is required by PIP module

    ./configure
    make
    ./python --version # should show Python ${PYTHON_VERSION}


Create python virtual environment
---------------------------------

.. code-block:: bash

    #!/bin/bash

    sudo ${PYTHON_INTERPRETER_PATH}/python -m venv /opt/python3.6-ciur


Then use ``/opt/python3.6-ciur/bin/python`` as a default python interpreter in your IDE (f.e. PyCharm)


Install requirements
--------------------

.. code-block:: bash

    #!/bin/bash
    # script: install_requirements

    PYTHON_CIUR=/opt/python3.6-ciur/bin
    ${PYTHON_CIUR}/pip install --upgrade pip setuptools
    apt-get install -y --force-yes $(curl "https://bitbucket.org/ada/python-ciur/raw/python3.6-ciur/requirements-apt-get.txt" | grep -oP "^[^#\s]+")

    ${PYTHON_CIUR}/pip install -r "https://bitbucket.org/ada/python-ciur/raw/python3.6-ciur/requirements-pip.txt"
