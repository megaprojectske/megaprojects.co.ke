from django import utils
from django.core import urlresolvers
from django.db import models

from core import models as core_models
from core import utils as core_utils
from programs import models as program_models
import managers
import utils as article_utils


class Article(core_models.TimeStampedModel, core_models.BaseModel,
              core_models.AuthorModel, core_models.PublicModel,
              core_models.CommentModel):

    STATUS_DRAFT = 'd'
    STATUS_PUBLISHED = 'p'
    STATUS_WITHDRAWN = 'w'

    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_WITHDRAWN, 'Withdrawn'),
    ]

    KIND_ARTICLE = 'a'
    KIND_BLOG = 'b'
    KIND_FEATURE = 'f'

    KIND_CHOICES = [
        (KIND_ARTICLE, 'Article'),
        (KIND_BLOG, 'Blog'),
        (KIND_FEATURE, 'Feature'),
    ]

    pubdate = models.DateTimeField('publication date',
                                   default=utils.timezone.now())
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    lead = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    program = models.ForeignKey(program_models.Program, blank=True, null=True)

    objects = managers.ArticleManager()

    def get_absolute_url(self):
        return urlresolvers.reverse('article_detail',
                                    kwargs={'id': self.id, 'slug': self.slug})

    @property
    def thumbnail(self):
        thumbnail = self.image_set.filter(status=True).filter(thumbnail=True)
        # 'thumbnail' field is unique
        return thumbnail.get() if thumbnail else None

    class Meta:
        ordering = ['-pubdate']


# Keep the 'thumbnail' field unique for the images of each article
@core_utils.unique_boolean('thumbnail', subset=['article'])
class Image(core_models.TimeStampedModel, core_models.BaseModel,
            core_models.ImageModel):
    image = models.ImageField(upload_to=article_utils.get_image_path)
    article = models.ForeignKey(Article)

    objects = managers.ImageManager()

    def __unicode__(self):
        return self.shortuuid

    class Meta:
        ordering = ['-article__pubdate', '-created']
