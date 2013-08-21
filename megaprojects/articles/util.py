def get_image_path(instance, filename):
    import re

    folder_name = '%s/%s' % ('articles', instance.article.id)
    extension = re.search(r'\.[^.]+$', filename)
    filename = str(instance.shortuuid) + extension.group(0)

    return '%s/%s' % (folder_name, filename)