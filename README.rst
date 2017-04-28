=============================
django-logmail
=============================

.. image:: https://badge.fury.io/py/django-logmail.svg
    :target: https://badge.fury.io/py/django-logmail

.. image:: https://travis-ci.org/pycodi/django-logmail.svg?branch=master
    :target: https://travis-ci.org/pycodi/django-logmail

.. image:: https://codecov.io/gh/pycodi/django-logmail/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/pycodi/django-logmail

Django email backend that logs all emails

Documentation
-------------

The full documentation is at https://django-logmail.readthedocs.io.

Quickstart
----------

Install django-logmail::

    pip install django-logmail

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'logmail.apps.LogmailConfig',
        ...
    )

Add django-logmail's URL patterns:

.. code-block:: python

    from logmail import urls as logmail_urls


    urlpatterns = [
        ...
        url(r'^', include(logmail_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
