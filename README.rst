=============
Django-Emails
=============

CRUD app for collecting email addresses

Quick start
-----------

1. Add "emails" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'emails',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('emails/', include('emails.urls')),

3. Run ``python manage.py migrate`` to create the emails models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/emails/ to participate in the poll.