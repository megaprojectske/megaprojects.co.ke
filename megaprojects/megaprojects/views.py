from django.views import generic

from articles import models


class FrontPageView(generic.TemplateView):

    template_name = "frontpage/index.html"

    def get_context_data(self, **kwargs):
        context = super(FrontPageView, self).get_context_data(**kwargs)

        article_list = [
            article for article in models.Article.objects.articles().published()[:15]]
        image_list = [
            image for image in models.Image.objects.articles().published()[:12]]

        context['article_list'] = article_list
        context['image_list'] = image_list

        return context
