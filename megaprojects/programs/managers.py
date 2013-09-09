from django.db import models

import mixins
import query


class ProgramManager(models.Manager, mixins.ProgramManagerMixin):

    def get_query_set(self):
        return query.ProgramQuerySet(self.model, using=self._db)


class ImageManager(models.Manager, mixins.ImageManagerMixin):

    def get_query_set(self):
        return query.ImageQuerySet(self.model, using=self._db)
