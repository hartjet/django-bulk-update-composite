from django.db import models
from .helper import bulk_update


class BulkUpdateQuerySet(models.QuerySet):

    def bulk_update(self, objs, update_fields=None,
                    exclude_fields=None, batch_size=None, pk_field='pk', extra_clauses=''):

        self._for_write = True
        using = self.db

        return bulk_update(
            objs, update_fields=update_fields,
            exclude_fields=exclude_fields, using=using,
            batch_size=batch_size, pk_field=pk_field, extra_clauses=extra_clauses)
