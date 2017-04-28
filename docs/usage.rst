=====
Usage
=====

To use django-logmail in a project, add it to your `INSTALLED_APPS`:

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
