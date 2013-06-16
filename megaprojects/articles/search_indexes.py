from haystack import indexes

import models


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return models.Article

    def index_queryset(self, using=None):
        return self.get_model().objects.published()
