==========================
Python virtual environment
==========================

We will use only python version 3.5

Compile python it from source code
----------------------------------

In case you don not have it, follow bellow instructions to compile it from source code.

.. code-block:: bash

    #!/bin/bash
    # script: compile_python_3_5

    cd /opt
    wget --version || apt-get install -y wget # install wget in case is not present
    wget -c https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tar.xz

    xz --version || apt-get install -y xz-utils  # install xz in case is not present
    tar xf Python-3.5.2.tar.xz
    cd Python-3.5.2/
    gcc --version || apt-get install -y build-essential  # install xz in case is not present
    apt-get install -y libssl-dev # ssl is required by PIP module
    ./configure
    make
    ./python --version # should show Python 3.5.2


Create virtual python3.5 virtual environment
--------------------------------------------

.. code-block:: bash

    #!/bin/bash

    sudo ${PYTHON_INTERPRETER_PATH}/python -m venv /opt/python3-ciur


Then use ``/opt/python3-ciur/bin/python`` as a default python interpreter in your IDE (f.e. PyCharm)


Install requirements
--------------------

.. code-block:: bash

    #!/bin/bash
    # script: install_requirements

    PYTHON3_CIUR=/opt/python3-ciur/bin
    sudo ${PYTHON3_CIUR}/pip install --upgrade pip setuptools
    sudo apt-get install -y --force-yes $(cat requirements-apt-get.txt | grep -oP "^[^#\s]+")
    sudo ${PYTHON3_CIUR}/pip install -r requirements-pip.txt
