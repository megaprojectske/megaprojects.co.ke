from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from core.models import TimeStampedModel, BaseModel, AuthorModel, PublicModel, ImageModel, CommentModel
from core.util import unique_boolean
from programs.models import Program

from .managers import ArticleManager, ImageManager
import util


STATUS_CHOICES = [('d', 'Draft'),  ('p', 'Published'), ('w', 'Withdrawn')]
KIND_CHOICES = [('a', 'Article'), ('f', 'Feature')]


class Article(TimeStampedModel, BaseModel, AuthorModel, PublicModel, CommentModel):

    pubdate = models.DateTimeField('publication date', default=timezone.now())
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    lead = models.CharField(max_length=255, blank=True)
    body = models.TextField()

    program = models.ForeignKey(Program, blank=True, null=True)
    objects = ArticleManager()

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'id': self.id, 'slug': self.slug})

    @property
    def thumbnail(self):
        thumbnail = self.image_set.filter(status=True).filter(thumbnail=True)
        # 'thumbnail' field is unique
        return thumbnail.get() if thumbnail else None

    class Meta:
        ordering = ['-pubdate']


# Keep the 'thumbnail' field unique for the images of each article
@unique_boolean('thumbnail', subset=['article'])
class Image(TimeStampedModel, BaseModel, ImageModel):

    image = models.ImageField(upload_to=util.get_image_path)

    article = models.ForeignKey(Article)
    objects = ImageManager()

    class Meta:
        ordering = ['-article__pubdate', '-created']
