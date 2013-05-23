from django.core.management.base import BaseCommand

import _titlecase as titlecase

from articles.models import Article
from blog.models import Post
from programs.models import Program


# This command is silly if you think about it ...
class Command(BaseCommand):
    help = 'Uses the titlecase package to capitalize Article, Post & Program titles.'

    def handle(self, *args, **options):
        for article in Article.objects.all():
            article.title = titlecase.titlecase(article.title)
            article.save()

        self.stdout.write('Successfully processed Article')

        for post in Post.objects.all():
            post.title = titlecase.titlecase(post.title)
            post.save()

        self.stdout.write('Successfully processed Post')

        for program in Program.objects.all():
            program.title = titlecase.titlecase(program.title)
            program.save()

        self.stdout.write('Successfully processed Program')
