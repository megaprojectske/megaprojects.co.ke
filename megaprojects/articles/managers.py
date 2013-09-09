from django.db import models

import mixins
import query


class ArticleManager(models.Manager, mixins.ArticleManagerMixin):

    def get_query_set(self):
        return query.ArticleQuerySet(self.model, using=self._db)


class ImageManager(models.Manager, mixins.ImageManagerMixin):

    def get_query_set(self):
        return query.ImageQuerySet(self.model, using=self._db)
