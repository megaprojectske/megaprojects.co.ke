from django.core.management import base

import _titlecase as titlecase

from articles.models import Article
from programs.models import Program


# This command is silly if you think about it ...
class Command(base.BaseCommand):
    args = 'a (Article), or p (Program)'
    help = 'Uses the titlecase package to capitalize article (a), or program (p) titles.'

    def handle(self, *args, **options):

        if not len(args):
            raise base.CommandError('No valid arguments specified')

        kind = args[0]

        if kind == 'a':
            models = Article.objects.all()
        elif kind == 'p':
            models = Program.objects.all()
        else:
            raise base.CommandError('No valid arguments specified')

        for model in models:
            model.title = titlecase.titlecase(model.title)
            model.save()

        self.stdout.write('Successfully capitalized titles!')
