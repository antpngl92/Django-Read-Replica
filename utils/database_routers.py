from django.conf import settings
from django.contrib.auth.models import User


def read_replica_or_default() -> str:
    if settings.USE_READ_REPLICA:
        return settings.READ_REPLICA_DATABASE_NAME
    return 'default'


class DjangoModelsRouter:
    route_app_labels = {'article'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read models from route_app_labels list
        go to a database evaluated by read_replica_or_default() util.
        """
        if model._meta.app_label in self.route_app_labels:
            return read_replica_or_default()

        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write all models go to default/main database.
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Objects from REPLICA and DEFAULT are de same, then always True
        """
        return True



class CustomDatabaseRouter:
    router_app_labels = {'user', 'contenttypes'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read models from route_app_labels list go to a database users
        """
        if model._meta.app_label in self.route_app_labels:
            return 'users'

        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write all models go to default/main database.
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Objects from REPLICA and DEFAULT are de same, then always True
        """
        return True


    def allow_migrate(db, app_label, model_name=None, **hints):
        """
        Determine if the migration operation is allowed to run on the database
        with alias db. Return True if the operation should run, False if it
        shouldn’t run, or None if the router has no opinion.
        """
        return None



