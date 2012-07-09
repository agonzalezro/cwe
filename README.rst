.. note:: This is a proof of concept to show how to access to the
          information needed at the project `"Common Welfare Economy" (aka
          Gemeinwohl-Ökonomie) <http://www.gemeinwohl-oekonomie.org/en/>`_.

The project was developed with django and it is a very basic project that
allows you to:

- store information on the DB: companies, individual people, organizations &
  politicians.
- access to this information via an API developed with tastypie.


Installation
------------

Create a virtualenv, or install the packages system-wide with::

    $ pip install -r requirements.txt


Creating DB
-----------

By default it will create a sqlite DB for you, feel free to change it on the
`settings.py` file::

    $ python manage.py syncdb


Usage
-----

I will not explain here how to deploy a wsgi application :) But if you want
to check the app with the dev server::

    $ python manage.py runserver


Example of API
--------------

After run the server you can access to this URL:
http://127.0.0.1:8000/api/v1/company?format=json and it will return to you
this JSON format::

    {"meta": {"limit": 20,
              "next": null,
              "offset": 0,
              "previous": null,
              "total_count": 1},
     "objects": [{"address": "Groningen",
                  "employees": 70,
                  "id": "1",
                  "name": "Paylogic",
                  "resource_uri": "/api/v1/company/1/",
                  "url": "http://paylogic.nl/"}]
    }
