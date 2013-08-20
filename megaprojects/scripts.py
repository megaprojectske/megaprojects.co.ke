def import_drupal_nodes(file_path):
    import csv
    from datetime import datetime
    from articles.models import Article
    from programs.models import Program

    with open(file_path, 'r') as csv_file:
        for counter, row in enumerate(csv.reader(csv_file, delimiter=';', quotechar='"')):
            row_nid = int(row[0])
            row_title = row[1]
            row_status = 'p' if int(row[2]) else 'd'
            row_created = int(row[3])
            row_body = row[4]
            row_project = row[5]

            program, created = Program.objects.get_or_create(
                title=row_project,
            )

            Article(
                author_id=1,
                body=row_body,
                drupal_id=row_nid,
                kind='a',
                program=program,
                pubdate=datetime.fromtimestamp(row_created),
                status=row_status,
                title=row_title,
            ).save()


def migrate_uuid_shortuuid(model):
    from articles import models as amodels
    from blog import models as bmodels
    from programs import models as pmodels

    if model == 'a':
        for article in amodels.Article.objects.all():
            for image in article.image_set.all():
                # Generate the shortuuid
                image.save()

                # Replace the old tokens
                article.body = article.body \
                    .replace("<<<%s>>>" % image.uuid, "[image %s]" % image.shortuuid) \
                    .replace("[image %s]" % image.uuid, "[image %s]" % image.shortuuid)

            article.save()

    if model == 'b':
        for post in bmodels.Post.objects.all():
            for image in post.image_set.all():
                # Generate the shortuuid
                image.save()

                # Replace the old tokens
                post.body = post.body \
                    .replace("<<<%s>>>" % image.uuid, "[image %s]" % image.shortuuid) \
                    .replace("[image %s]" % image.uuid, "[image %s]" % image.shortuuid)

            post.save()

    if model == 'p':
        for program in pmodels.Program.objects.all():
            for image in program.image_set.all():
                # Generate the shortuuid
                image.save()

                # Replace the old tokens
                program.body = program.body \
                    .replace("<<<%s>>>" % image.uuid, "[image %s]" % image.shortuuid) \
                    .replace("[image %s]" % image.uuid, "[image %s]" % image.shortuuid)

            program.save()
