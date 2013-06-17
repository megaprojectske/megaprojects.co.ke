import uuid

from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):

    """
    An abstract base class model that provides self-updating ``created`` and
    ``modified`` fields.
    """

    created = models.DateTimeField(
        auto_now_add=True, help_text='The time when this entity was created.')
    changed = models.DateTimeField(
        auto_now=True, help_text='The time when this entity was most recently saved.')

    class Meta:
        abstract = True


class BaseModel(TimeStampedModel):

    """
    Abstract model for main entities. Provides a ``title`` and ``uuid`` field.
    """

    title = models.CharField(
        max_length=255, help_text='The title of this entity, always treated as non-markup plain text.')
    uuid = models.CharField('UUID', max_length=255, unique=True,
                            help_text='Unique Key: Universally unique identifier for this entity.')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class AuthorModel(BaseModel):

    """
    Builds upon ``BaseModel`` by adding a ``author`` field.
    """

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, help_text='The user that owns this entity; Initially, this is the user that created it.')

    class Meta:
        abstract = True


class ImageModel(BaseModel):

    """
    Abstract base class model for Image fields.
    """

    status = models.BooleanField(
        default=True, help_text='Boolean indicating whether the entity is published (visible to non-administrators).')
    reviewed = models.BooleanField(
        help_text='Object has been reviewed (quality control).')
    thumbnail = models.BooleanField(
        help_text='Boolean indicating whether the entity is the main model thumbnail.')

    def __unicode__(self):
        return self.uuid

    class Meta:
        abstract = True
