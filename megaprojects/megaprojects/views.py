from django.views.generic import TemplateView

from articles.models import Article


class FrontPageView(TemplateView):

    template_name = "frontpage/frontpage_detail.html"

    def get_context_data(self, **kwargs):
        context = super(FrontPageView, self).get_context_data(**kwargs)
        context['article_list'] = [article for article in Article.objects.all()[:12]]
        return context
