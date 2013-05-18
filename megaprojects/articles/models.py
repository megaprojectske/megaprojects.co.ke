from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from core.models import AuthorModel, ImageModel
from programs.models import Program

from .managers import ArticleManager, ImageManager
import util


STATUS_CHOICES = [('d', 'Draft'),  ('p', 'Published'), ('w', 'Withdrawn')]
KIND_CHOICES = [('a', 'Article'), ('f', 'Feature')]


class Article(AuthorModel):

    pubdate = models.DateTimeField('publication date', default=timezone.now())
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    lead = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    drupal_id = models.IntegerField('drupal NID', unique=True, blank=True,
                                    null=True, help_text='Node ID from the previous Drupal website (imported).')

    program = models.ForeignKey(Program, blank=True, null=True)

    objects = ArticleManager()

    @property
    def thumbnail(self):
        if self.image_set.all():
            return self.image_set.all()[:1].get()

    class Meta:
        ordering = ['-pubdate']


class Image(ImageModel):

    image = models.ImageField(upload_to=util.get_image_path)

    article = models.ForeignKey(Article)

    objects = ImageManager()

    class Meta:
        ordering = ['-article__pubdate', '-created']
