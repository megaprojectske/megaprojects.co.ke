from django.core import urlresolvers
from django.db import models

from core import models as core_models
from core import utils as core_utils
import managers
import utils


class Program(core_models.TimeStampedModel, core_models.BaseModel,
              core_models.PublicModel):

    abbr = models.CharField('abbreviation', max_length=255, blank=True)
    lead = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    status = models.BooleanField(
        help_text='Boolean indicating whether the entity is published (visible to non-administrators).')

    objects = managers.ProgramManager()

    def get_absolute_url(self):
        return urlresolvers.reverse('program_latest',
                                    kwargs={'id': self.id, 'slug': self.slug})

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
@core_utils.unique_boolean('thumbnail', subset=['program'])
class Image(core_models.TimeStampedModel, core_models.BaseModel,
            core_models.ImageModel):

    image = models.ImageField(upload_to=utils.get_image_path)
    program = models.ForeignKey(Program)

    objects = managers.ImageManager()

    class Meta:
        ordering = ['program__title', '-created']
