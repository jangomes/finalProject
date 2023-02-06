#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from multipleEcommerce.settings import base


def main():
    """Run administrative tasks."""

    if base.DEBUG:
        # this is the path to the manage.py file that I changed the name to local/production and the path to the settings file
        # I added .local(production) to the end of the settings file so you can run the server or the production server it depends on the debug mode
        # if debug is true it will run the local server if debug is false it will run the production server
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'multipleEcommerce.settings.local')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'multipleEcommerce.settings.production')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
