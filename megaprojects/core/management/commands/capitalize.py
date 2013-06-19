from django.core.management.base import BaseCommand, CommandError

import _titlecase as titlecase

from articles.models import Article
from blog.models import Post
from programs.models import Program


# This command is silly if you think about it ...
class Command(BaseCommand):
    args = 'a (Article), b (Post) or p (Program)'
    help = 'Uses the titlecase package to capitalize article (a), post (b) or program (p) titles.'

    def handle(self, *args, **options):

        if not len(args):
            raise CommandError('No valid arguments specified')

        kind = args[0]

        if kind == 'a':
            models = Article.objects.all()
        elif kind == 'b':
            models = Post.objects.all()
        elif kind == 'p':
            models = Program.objects.all()
        else:
            raise CommandError('No valid arguments specified')

        for model in models:
            model.title = titlecase.titlecase(model.title)
            model.save()

        self.stdout.write('Successfully capitalized titles!')
