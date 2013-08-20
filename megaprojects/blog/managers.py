from django.db import models


class PostManager(models.Manager):

    def draft(self):
        return self.model.objects.filter(status='d')

    def published(self):
        return self.model.objects.filter(status='p')


class ImageManager(models.Manager):

    def draft(self):
        return self.model.objects.filter(status=True).filter(post__status='d')

    def published(self):
        return self.model.objects.filter(status=True).filter(post__status='p')
