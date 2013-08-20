from django.views.generic import ListView

from core.views import PublicDetailView
from .models import Post


class PostListView(ListView):

    queryset = Post.objects.published()
    paginate_by = 8


class PostDetailView(PublicDetailView):

    model = Post
