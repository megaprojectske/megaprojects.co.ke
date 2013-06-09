from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):

    model = Article
    paginate_by = 8

    def get_queryset(self):
        # Check that status = 'p' (Published)
        return Article.objects.published()


class ArticleDetailView(DetailView):

    model = Article

    def get_queryset(self):
        # Check that the status = 'p' (Published)
        self.article = get_object_or_404(
            Article, pk=self.kwargs.get('pk'), status='p')
        return super(ArticleDetailView, self).get_queryset()
