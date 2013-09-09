# See: http://hunterford.me/django-custom-model-manager-chaining/


class ProgramManagerMixin(object):

    def published(self, status=True):
        return self.filter(status=status)


class ImageManagerMixin(object):

    def published(self, status=True):
        return self.filter(program__status=True).filter(status=status)
