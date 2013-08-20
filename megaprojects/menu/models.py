import ast

from django.core.urlresolvers import reverse, NoReverseMatch
from django.db import models

from core.models import TimeStampedModel, TitleModel


class Menu(TimeStampedModel, TitleModel):

    slug = models.CharField(max_length=255, unique=True)
    enabled = models.BooleanField(default=True)

    @property
    def links(self):
        return self.link_set.filter(enabled=True).filter(parent=None)

    class Meta:
        ordering = ['title']


class Link(TimeStampedModel, TitleModel):

    url = models.CharField('URL', max_length=255, blank=True)
    order = models.IntegerField(default=0)
    enabled = models.BooleanField(default=True)

    view_name = models.CharField(max_length=255, blank=True)
    args = models.CharField(max_length=255, default='[]', blank=True)
    kwargs = models.CharField(max_length=255, default='{}', blank=True)

    parent = models.ForeignKey('self', blank=True, null=True)
    menu = models.ForeignKey(Menu, blank=True, null=True)

    def __unicode__(self):
        if self.parent:
            return "%s - %s" % (self.parent.title, self.title)
        if self.menu:
            return "%s - %s" % (self.menu.title, self.title)
        else:
            return self.title

    @property
    def has_children(self):
        return self.link_set.filter(enabled=True).exists()

    @property
    def children(self):
        return self.link_set.filter(enabled=True)

    @property
    def href(self):
        if self.url:
            return self.url
        else:
            try:
                args = ast.literal_eval(self.args)
                kwargs = ast.literal_eval(self.kwargs)
                return reverse(self.view_name, args=args, kwargs=kwargs)
            except (NoReverseMatch, ValueError):
                return '#'

    class Meta:
        ordering = ['menu', 'order', 'title']
