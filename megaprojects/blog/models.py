from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from core.models import TimeStampedModel, BaseModel, AuthorModel, PublicModel, ImageModel, CommentModel
from core.utils import unique_boolean

from .managers import PostManager, ImageManager
import util


STATUS_CHOICES = [('d', 'Draft'),  ('p', 'Published'), ('w', 'Withdrawn')]


class Post(TimeStampedModel, BaseModel, AuthorModel, PublicModel, CommentModel):

    pubdate = models.DateTimeField('publication date', default=timezone.now())
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    body = models.TextField()

    objects = PostManager()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'id': self.id, 'slug': self.slug})

    @property
    def thumbnail(self):
        thumbnail = self.image_set.filter(status=True).filter(thumbnail=True)
        # 'thumbnail' field is unique
        return thumbnail.get() if thumbnail else None

    class Meta:
        ordering = ['-pubdate']


# Keep the 'thumbnail' field unique for the images of each post
@unique_boolean('thumbnail', subset=['post'])
class Image(TimeStampedModel, BaseModel, ImageModel):

    image = models.ImageField(upload_to=util.get_image_path)

    post = models.ForeignKey(Post)
    objects = ImageManager()

    class Meta:
        ordering = ['-post__pubdate', '-created']
