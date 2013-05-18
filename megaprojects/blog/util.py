def get_image_path(instance, filename):
    import re

    folder_name = '%s/%s' % ('posts', instance.article.uuid)
    extension = re.search(r'\.[^.]+$', filename)
    filename = str(instance.uuid) + extension.group(0)

    return '%s/%s' % (folder_name, filename)
