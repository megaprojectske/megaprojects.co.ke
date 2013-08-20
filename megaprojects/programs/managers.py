from django.db import models


class ProgramManager(models.Manager):

    def published(self):
        return self.model.objects.filter(status=True)

    def unpublished(self):
        return self.model.objects.filter(status=False)


class ImageManager(models.Manager):

    def published(self):
        return self.model.objects.filter(status=True).filter(program__status=True)

    def unpublished(self):
        return self.model.objects.filter(status=True).filter(program__status=False)
