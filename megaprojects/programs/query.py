from django.db.models import query

import mixins


class ProgramQuerySet(query.QuerySet, mixins.ProgramManagerMixin):
    pass


class ImageQuerySet(query.QuerySet, mixins.ImageManagerMixin):
    pass
