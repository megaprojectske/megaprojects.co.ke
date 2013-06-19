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


# def import_drupal_files(file_path):
#     import csv
#     import os.path
#     from django.core.files.base import ContentFile
#     from articles.models import Article, Image
#     from articles import util

#     with open(file_path, 'r') as csv_file:
#         for counter, row in enumerate(csv.reader(csv_file, delimiter=';', quotechar='"')):
#             row_fid = int(row[0])
#             row_uri = row[1]
#             row_nid = int(row[2])

#             try:
#                 article = Article.objects.get(drupal_id=row_nid)
#             except Article.DoesNotExist:
#                 print "NID does not exist %d" % (counter + 1)
#                 continue

#             if article.image_set.all():
#                 print "Other image(s) exist %d" % (counter + 1)
#                 continue

#             if os.path.isfile(row_uri):
#                 with open(row_uri, 'r') as content_file:
#                     content = ContentFile(content_file.read())
#                     image_model = Image()
#                     image_model.article = article
#                     image_model.save()
#                     image_model.image.save(util.get_image_path(
#                         image_model, content_file.name), content)
#                     print "Success %d" % (counter + 1)
#             else:
#                 print "Does not exist %d " % (counter + 1)


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
