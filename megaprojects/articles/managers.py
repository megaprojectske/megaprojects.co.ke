from django.db import models


class ArticleManager(models.Manager):

    def draft(self):
        return self.model.objects.filter(status='d')

    def published(self):
        return self.model.objects.filter(status='p')


class ImageManager(models.Manager):

    def draft(self):
        return self.model.objects.filter(status=True).filter(article__status='d')

    def published(self):
        return self.model.objects.filter(status=True).filter(article__status='p')
