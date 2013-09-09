from django import shortcuts
from django.views import generic


class PublicDetailView(generic.DetailView):

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        obj = shortcuts.get_object_or_404(queryset, pk=self.kwargs.get('id'),
                                          status='p')

        return obj

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.get_absolute_url() != self.request.path:
            return shortcuts.redirect(self.object, permanent=True)

        # See: super(PublicDetailView, self).get(request, *args, **kwargs)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

        # TODO: Find a way to call super() without retrieving the object twice
        # super(PublicDetailView, self).get(request, *args, **kwargs)
