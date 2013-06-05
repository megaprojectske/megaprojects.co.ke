from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from core.models import AuthorModel, ImageModel
from core.util import unique_boolean

from .managers import PostManager, ImageManager
import util


STATUS_CHOICES = [('d', 'Draft'),  ('p', 'Published'), ('w', 'Withdrawn')]


class Post(AuthorModel):

    pubdate = models.DateTimeField('publication date', default=timezone.now())
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    body = models.TextField()
    drupal_id = models.IntegerField('drupal NID', unique=True, blank=True,
                                    null=True, help_text='Node ID from the previous Drupal website (imported).')

    objects = PostManager()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    @property
    def thumbnail(self):
        thumbnail = self.image_set.filter(status=True).filter(thumbnail=True)
        # 'thumbnail' field is unique
        return thumbnail.get() if thumbnail else None

    class Meta:
        ordering = ['-pubdate']


# Keep the 'thumbnail' field unique for the images of each post
@unique_boolean('thumbnail', subset=['post'])
class Image(ImageModel):

    image = models.ImageField(upload_to=util.get_image_path)

    post = models.ForeignKey(Post)

    objects = ImageManager()

    class Meta:
        ordering = ['-post__pubdate', '-created']
