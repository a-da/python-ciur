====
Ciur
====

.. image:: https://magnum-ci.com/status/8fa4d3425c370586324393b7ad167d41.png
   :target: https://magnum-ci.com/projects/4535
   :alt: Build Status fom magnum-ci.com
   
.. image:: ./docs/images/wooden-sieve-old-ancient-isolated-white-background.jpg
   :target: https://bitbucket.org/ada/python-ciur
   :alt: Ciur

..

    *Ciur is a scrapper layer in development*

    *Ciur is a lib because it has less black magic than a framework*


It exports all scrapper related code into separate layer.

If you are annoyed by
`Spaghetti code <https://en.wikipedia.org/wiki/Spaghetti_code>`_,
sql inside php and inline css inside html
THEN you also are annoyed by xpath/css code inside crawler.

Samples of `bad code <./docs/bad_code/>`_.

Ciur gives the taste of `Lasagna code <http://c2.com/cgi/wiki?LasagnaCode>`_
generally by enforcing encapsulation for scrapping layer.

What does “Ciur” mean?
======================

Ciur is Romanian for `Sieve <https://en.wikipedia.org/wiki/Sieve>`_.

It fulfils the same purpose in the sense of being a
"device for separating wanted elements from unwanted material".

Ciur use MIT License
====================
This means that code may be included in proprietary code without any additional restrictions.

Please see `LICENSE <./LICENSE>`_.

End-User Documentation
======================

Ciur uses own dsl, for example

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

    >>> import ciur
    >>> from ciur.shortcuts import pretty_parse_from_url
    >>> with ciur.open_file("example.org.ciur", __file__) as f:
    ...    print pretty_parse_from_url(
    ...            f,
    ...            "http://example.org"
    ...    )    
    {
         "root": {
             "name": "Example Domain",
             "paragraph": "This domain is established to be used for illustrative examples in documents. You may use this\n    domain in examples without prior coordination or asking for permission."
         }
     }


Samples of usage:
   * https://bitbucket.org/ada/ciur.example.exchange --> parsing world wide (40 sources, 4 country) currency exchange rates.
   * https://bitbucket.org/ada/ciur.example.social --> parsing networking sites (such as Facebook, Linkedin, Xing ...) (not yet ready for open realease)

Developer Guide
===============


Install
=======

Install virtualenv

.. code-block :: bash

    $ sudo virtualenv -p python2 /opt/python-env/ciur_env/
    [sudo] password for ada: 
    Running virtualenv with interpreter /usr/bin/python2
    New python executable in /opt/python-env/ciur_env/bin/python2
    Also creating executable in /opt/python-env/ciur_env/bin/python
    Installing setuptools, pip, wheel...done.

Install ciur in virtualenv

.. code-block :: bash

    $ sudo /opt/python-env/ciur_env2/bin/pip install  git+https://bitbucket.org/ada/python-ciur.git#egg=ciur  
    ...
    Successfully installed cffi-1.4.2 ciur-0.1.2 cryptography-1.1.2 
    cssselect-0.9.1 enum34-1.1.2 html5lib-0.9999999 idna-2.0 ipaddress-1.0.16 
    lxml-3.5.0 ndg-httpsclient-0.4.0 pdfminer-20140328 pyOpenSSL-0.15.1 
    pyasn1-0.1.9 pycparser-2.14 pyparsing-2.0.7 python-dateutil-2.4.2 
    requests-2.9.1 six-1.10.0
    ...

.. Features
   ========

   The ``ciur`` can do a lot.

   Please see `list of all features <./features.rst>`_.


TODO:
=====
 
 * TODO: http://lybniz2.sourceforge.net/safeeval.html
 * demo on cloud9
 * build documentation on readthedocs 
 * http://lxml.de/lxmlhtml.html#parsing-html

   .cssselect(expr):

   .base_url:

.. ====== Last Mile
   https://youtu.be/FVEEndIwOSA?t=2243
