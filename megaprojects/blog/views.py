from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):

    model = Post
    paginate_by = 8

    def get_queryset(self):
        # Check that status = 'p' (Published)
        return Post.objects.published()


class PostDetailView(DetailView):

    model = Post

    def get_queryset(self):
        # Check that status = 'p' (Published)
        self.article = get_object_or_404(
            Post, pk=self.kwargs.get('pk'), status='p')
        return super(PostDetailView, self).get_queryset()
