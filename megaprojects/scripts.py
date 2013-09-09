def migrate_posts_to_articles():
    from django.core.files import base
    from articles.models import Article, Image
    from blog.models import Post

    for p in Post.objects.all():
        a = Article()

        a.author = p.author
        a.body = p.body
        a.enable_comments = p.enable_comments
        a.pubdate = p.pubdate
        a.reviewed = p.reviewed
        a.title = p.title

        a.save()

        if p.status:
            a.status = 'p'
        else:
            a.status = 'd'

        for pi in p.image_set.all():
            ai = Image()

            ai.article = a
            ai.image = base.ContentFile(pi.image.read())
            ai.reviewed = pi.reviewed
            ai.shortuuid = pi.shortuuid
            ai.status = pi.status
            ai.thumbnail = pi.thumbnail
            ai.title = pi.title

            ai.save()
