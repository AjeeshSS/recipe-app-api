""" Django command to wait for the database to be available """


import time

from psycopg2 import OperationalError as psycopg2operror

from django.db.utils import OperationalError
# Error django throws when database is not ready
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """  Command to wait for the database """

    def handle(self, *args, **options):
        """  Encrypted for command """
        self.stdout.write('waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2operror, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
