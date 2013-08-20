from django.contrib.syndication.views import Feed

from articles.models import Article


class FrontPageFeed(Feed):

    description = 'Updates on changes and additions to www.megaprojects.co.ke'
    description_template = 'feeds/article_body.html'
    link = '/'
    # TODO: Move title to settings
    title = 'MegaProjects Kenya - All Posts'

    def items(self):
        return Article.objects.published()[:10]

    def item_title(self, item):
        return item.title
