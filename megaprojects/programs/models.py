from django.core.urlresolvers import reverse
from django.db import models

from core.models import BaseModel, ImageModel
from core.util import unique_boolean

from .managers import ProgramManager, ImageManager
import util


class Program(BaseModel):

    abbr = models.CharField('abbreviation', max_length=255, blank=True)
    lead = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    status = models.BooleanField(
        help_text='Boolean indicating whether the entity is published (visible to non-administrators).')
    reviewed = models.BooleanField(
        help_text='Program has been reviewed (quality control).')

    objects = ProgramManager()

    def get_absolute_url(self):
        return reverse('program_latest', kwargs={'pk': self.pk})

    @property
    def thumbnail(self):
        thumbnail = self.image_set.filter(status=True).filter(thumbnail=True)
        # 'thumbnail' field is unique
        return thumbnail.get() if thumbnail else None

    class Meta:
        ordering = ['title']


class Detail(models.Model):

    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    program = models.ForeignKey(Program)

    def __unicode__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'program'


# Keep the 'thumbnail' field unique for the images of each program
@unique_boolean('thumbnail', subset=['program'])
class Image(ImageModel):

    image = models.ImageField(upload_to=util.get_image_path)

    program = models.ForeignKey(Program)

    objects = ImageManager()

    class Meta:
        ordering = ['program__title', '-created']
