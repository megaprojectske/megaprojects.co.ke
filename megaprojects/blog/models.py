from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from core.models import AuthorModel, ImageModel

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
        if self.image_set.published().filter(post=self):
            return self.image_set.published().filter(post=self)[:1].get()

    class Meta:
        ordering = ['-pubdate']


class Image(ImageModel):

    image = models.ImageField(upload_to=util.get_image_path)

    post = models.ForeignKey(Post)

    objects = ImageManager()

    class Meta:
        ordering = ['-post__pubdate', '-created']
