from django.views.generic import TemplateView

from articles.models import Article, Image
from blog.models import Post


class FrontPageView(TemplateView):

    template_name = "frontpage/index.html"

    def get_context_data(self, **kwargs):
        context = super(FrontPageView, self).get_context_data(**kwargs)

        context['article_list'] = [
            article for article in Article.objects.published()[:14]]
        context['popular_list'] = context['article_list'][:8]
        context['image_list'] = [
            image for image in Image.objects.published()[:12]]
        context['post_list'] = [
            article for article in Post.objects.published()[:5]]

        return context
