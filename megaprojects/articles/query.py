from django.db.models import query

import mixins


class ArticleQuerySet(query.QuerySet, mixins.ArticleManagerMixin):
    pass


class ImageQuerySet(query.QuerySet, mixins.ImageManagerMixin):
    pass
