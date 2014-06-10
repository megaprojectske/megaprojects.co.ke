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


def move_article_image_files(article_image=None):
    if not article_image:
        from articles.models import Image as ArticleImage

        REGEX_UUID = r'[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}/[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}'
        articles_images = ArticleImage.objects.filter(image__regex=REGEX_UUID)
        print 'Processing %d images' % len(articles_images)

        for ai in articles_images:
            move_article_image_files(ai)
            print 'Done!'
    else:
        from django.core.files.storage import default_storage
        from articles.utils import get_image_path

        luuid_path = article_image.image.name
        suuid_path = get_image_path(article_image, luuid_path)

        # Check if destination exists
        if default_storage.exists(suuid_path):
            print 'Error: Destination exists (ID: %d)' % article_image.id
            return

        # Copy luuid path to suuid path
        im = default_storage.open(luuid_path, 'r')
        default_storage.save(suuid_path, im)

        # Save suuid path
        article_image.image = suuid_path
        article_image.save()

        # Delete luuid path
        default_storage.delete(luuid_path)


def move_program_image_files(program_image=None):
    if not program_image:
        from programs.models import Image as ProgramImage

        REGEX_UUID = r'[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}/[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}'
        program_images = ProgramImage.objects.filter(image__regex=REGEX_UUID)
        print 'Processing %d images' % len(program_images)

        for pi in program_images:
            move_program_image_files(pi)
            print 'Done!'
    else:
        from django.core.files.storage import default_storage
        from programs.utils import get_image_path

        luuid_path = program_image.image.name
        suuid_path = get_image_path(program_image, luuid_path)

        # Check if destination exists
        if default_storage.exists(suuid_path):
            print 'Error: Destination exists (ID: %d)' % program_image.id
            return

        # Copy luuid path to suuid path
        im = default_storage.open(luuid_path, 'r')
        default_storage.save(suuid_path, im)

        # Save suuid path
        program_image.image = suuid_path
        program_image.save()

        # Delete luuid path
        default_storage.delete(luuid_path)
