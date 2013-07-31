from django.views.generic import ListView

from core.views import PublicDetailView
from .models import Post


class PostListView(ListView):

    # Check that status = 'p' (Published)
    queryset = Post.objects.published()
    paginate_by = 5


class PostDetailView(PublicDetailView):

    model = Post
