def migrate_posts_to_articles():
    from articles.models import Article
    from blog.models import Post

    for p in Post.objects.all():
        try:
            Article.objects.get(shortuuid=p.shortuuid)
            continue
        except Article.DoesNotExist:
            a = Article()
            a.author = p.author
            a.body = p.body
            a.changed = p.changed
            a.created = p.created
            a.enable_comments = p.enable_comments
            a.kind = Article.KIND_BLOG
            a.pubdate = p.pubdate
            a.reviewed = p.reviewed
            a.shortuuid = p.shortuuid
            a.slug = p.slug
            a.status = Article.STATUS_PUBLISHED if p.status else Article.STATUS_DRAFT
            a.title = p.title
            a.uuid = p.uuid
            a.save()


def migrate_post_images_to_article_images():
    from django.core.files import base
    from articles.models import Article, Image as ArticleImage
    from blog.models import Post, Image as PostImage

    for pi in PostImage.objects.all():
        try:
            a = Article.objects.get(
                kind=Article.KIND_BLOG, shortuuid=pi.post.shortuuid)
            try:
                ai = ArticleImage()
                ai.article = a
                ai.changed = pi.changed
                ai.created = pi.created
                ai.image = base.ContentFile(pi.image.read())
                ai.reviewed = pi.reviewed
                ai.save()
                ai.shortuuid = pi.shortuuid
                ai.status = pi.status
                ai.thumbnail = pi.thumbnail
                ai.title = pi.title
                ai.uuid = pi.uuid
                ai.save()
            except IOError, e:
                print e
        except Article.DoesNotExist, e:
            print e
