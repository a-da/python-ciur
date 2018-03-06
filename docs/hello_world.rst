Install ciur
============

Lets assume that we using virtual env
(see `Python Virtual environment <https://bitbucket.org/ada/python-ciur/raw/python3.6-ciur/docs/python_virtual_environment.rst>`_)

.. code-block :: bash

    PIP=/opt/python-env/ciur_env/bin/pip
    CIUR=/opt/python-env/ciur_env/bin/ciur


Install branch python3.6-ciur with pip

.. code-block :: bash
    $ branch_name=python3-ciur  # you can find all available branches in bitbucket UI interface
    $ ${PIP} install "git+https://bitbucket.org/ada/python-ciur.git@${branch_name}#egg=ciur"
    # or for contribution purposes
    # ${PIP} install -e "/your/local/clone/of/ciur/branch"
    ...
    Successfully installed cffi-1.4.2 ciur-0.1.2 cryptography-1.1.2
    cssselect-0.9.1 enum34-1.1.2 html5lib-0.9999999 idna-2.0 ipaddress-1.0.16
    lxml-3.5.0 ndg-httpsclient-0.4.0 pdfminer-20140328 pyOpenSSL-0.15.1
    pyasn1-0.1.9 pycparser-2.14 pyparsing-2.0.7 python-dateutil-2.4.2
    requests-2.9.1 six-1.10.0
    ...


Type *"Hello word"*

.. code-block :: bash

    ${CIUR} --url "http://example.org" --rules="https://bitbucket.org/ada/python-ciur/raw/python3.6-ciur/docs/docker/example.org.ciur"

Based on ciur rules:

.. code-block:: bash

    $ curl "https://bitbucket.org/ada/python-ciur/raw/python3.6-ciur/docs/docker/example.org.ciur"
    root `/html/body` +1
        name `.//h1/text()` +1
        paragraph `.//p/text()` +1


We are going to receive parsed data as json:

.. code-block :: json

    {
        "root": {
            "name": "Example Domain",
            "paragraph": "This domain is established to be used for illustrative
                           examples in documents. You may use this
                           domain in examples without prior coordination or
                          asking for permission."
        }
    }
