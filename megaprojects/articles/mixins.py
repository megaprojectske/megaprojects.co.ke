# See: http://hunterford.me/django-custom-model-manager-chaining/


class ArticleManagerMixin(object):

    def published(self, status=True):
        if status:
            return self.filter(status='p')
        else:
            return self.filter(status='d')

    def articles(self):
        return self.filter(kind='a')

    def blog(self):
        return self.filter(kind='b')

    def featured(self):
        return self.filter(kind='f')


class ImageManagerMixin(object):

    def published(self, status=True):
        return self.filter(article__status='p').filter(status=status)

    def articles(self):
        return self.filter(article__kind='a')

    def blog(self):
        return self.filter(article__kind='b')

    def featured(self):
        return self.filter(article__kind='f')
