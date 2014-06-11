# See: http://hunterford.me/django-custom-model-manager-chaining/
import models


class ArticleManagerMixin(object):

    def published(self, status=True):
        if status:
            return self.filter(status=models.Article.STATUS_PUBLISHED)
        else:
            return self.filter(status=models.Article.STATUS_DRAFT)

    def articles(self):
        return self.filter(kind=models.Article.KIND_ARTICLE)

    def blog(self):
        return self.filter(kind=models.Article.KIND_BLOG)

    def featured(self):
        return self.filter(kind=models.Article.KIND_FEATURE)


class ImageManagerMixin(object):

    def published(self, status=True):
        return self.filter(article__status=models.Article.STATUS_PUBLISHED).filter(status=status)

    def articles(self):
        return self.filter(article__kind=models.Article.KIND_ARTICLE)

    def blog(self):
        return self.filter(article__kind=models.Article.KIND_BLOG)

    def featured(self):
        return self.filter(article__kind=models.Article.KIND_FEATURE)
