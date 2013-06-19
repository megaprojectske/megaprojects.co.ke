from django.views.generic import ListView

from core.views import PublicDetailView
from .models import Post


class PostListView(ListView):

    model = Post
    paginate_by = 5

    def get_queryset(self):
        # Check that status = 'p' (Published)
        return Post.objects.published()


class PostDetailView(PublicDetailView):

    model = Post
