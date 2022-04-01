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
