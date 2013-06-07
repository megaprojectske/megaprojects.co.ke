from django.contrib.syndication.views import Feed

from articles.models import Article


class FrontPageFeed(Feed):

    title = "MegaProjects Kenya - All Posts"
    link = "/"
    description = "Updates on changes and additions to megaprojects.co.ke."

    description_template = 'feeds/article_description.html'

    def items(self):
        return Article.objects.published()[:10]

    def item_title(self, item):
        return item.title
