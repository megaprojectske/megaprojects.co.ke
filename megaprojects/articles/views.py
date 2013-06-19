from django.views.generic import ListView

from core.views import PublicDetailView
from .models import Article


class ArticleListView(ListView):

    model = Article
    paginate_by = 8

    def get_queryset(self):
        # Check that status = 'p' (Published)
        return Article.objects.published()


class ArticleDetailView(PublicDetailView):

    model = Article
