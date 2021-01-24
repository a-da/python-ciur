Install ciur
============

.. code-block:: bash

    $ pip install ciur


Type *"Hello word"*

.. code-block:: bash

    $ ciur --url "http://example.org" --rules="https://bitbucket.org/ada/python-ciur/raw/python3.9-ciur/docs/docker/example.org.ciur"

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
