from django.views.generic import ListView

from core.views import PublicDetailView
from .models import Article


class ArticleListView(ListView):

    # Check that status = 'p' (Published)
    queryset = Article.objects.published()
    paginate_by = 8


class ArticleDetailView(PublicDetailView):

    model = Article
