from django.core.urlresolvers import reverse
from django.db import models

from core.models import BaseModel, ImageModel

from .managers import ProgramManager, ImageManager
import util


class Program(BaseModel):

    abbr = models.CharField('abbreviation', max_length=255, blank=True)
    status = models.BooleanField(
        help_text='Boolean indicating whether the entity is published (visible to non-administrators).')
    lead = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)

    objects = ProgramManager()

    def save(self, *args, **kwargs):
        super(Program, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']


class Detail(models.Model):

    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    program = models.ForeignKey(Program)

    def __unicode__(self):
        return self.key

    class Meta:
        order_with_respect_to = 'program'


class Image(ImageModel):

    image = models.ImageField(upload_to=util.get_image_path)

    program = models.ForeignKey(Program)

    objects = ImageManager()

    class Meta:
        ordering = ['program__title', '-created']
