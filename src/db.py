from postgres import Postgres
from os import environ


class DB:
    instance = None

    @staticmethod
    def make():
        if not DB.instance:
            DB.instance = Postgres(environ['JOBBR_DATABASE'] or '')
        return DB.instance
