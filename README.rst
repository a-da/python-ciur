====
Ciur
====

.. image:: http://thumbs.dreamstime.com/m/wooden-sieve-old-ancient-isolated-white-background-45140021.jpg
   :target: https://bitbucket.org/ada/ciur
   :alt: Ciur

..

    *Ciur is a scrapper layer in developing process.*

    *Ciur is a lib because it has less black magic than a framework*


Export all scrapper related code into separate layer.

If you are annoyed from sql spaghetti inside php and inline css inside html
THEN you also are annoyed from xpath/css code inside crawler.

Samples of `bad code <./docs/bad_code/>`_.

Ciur give you additional possibility to fix previous headache with adding additional layer.

What does “Ciur” mean?
======================
Ciur is an romanian word that means in english `Sieve <https://en.wikipedia.org/wiki/Sieve>`_.

It has the same purpose "device for separating wanted elements from unwanted material".

Ciur use MIT License
====================
This means that code may be included in proprietary code without any additional restrictions.

Please see `LICENSE <./LICENSE>`_.

End-User Documentation
======================

Ciur use own dsl, for example

.. code-block :: bash

     $ cat python-ciur/tests/ciur.d/example.org.ciur

.. code-block:: yaml

    root `/html/body` +1
        name `.//h1/text()` +1
        paragraph `.//p/text()` +1



Command Line Interface
----------------------

.. code-block :: bash

    $ ciur --url "http://example.org" --rules="example.org.ciur"
        

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


Python ciur API
---------------

    >>> import ciur.shortcuts
    >>> ciur.shortcuts.pretty_parse("example.org.ciur", "http://example.org")
    {
         "root": {
             "name": "Example Domain",
             "paragraph": "This domain is established to be used for illustrative examples in documents. You may use this\n    domain in examples without prior coordination or asking for permission."
         }
     }

Developer Guide
===============


Install
=======

>>> pip install git+https://bitbucket.org/ada/ciur.git#egg=ciur


TODO
====
DONE: type.method evaluation
TODO: http://lybniz2.sourceforge.net/safeeval.html
demo on cloud9
http://lxml.de/lxmlhtml.html#parsing-html
   .cssselect(expr):
   .base_url:


====== Last Mile
https://youtu.be/FVEEndIwOSA?t=2243