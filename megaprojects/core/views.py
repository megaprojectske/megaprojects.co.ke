from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView


class PublicDetailView(DetailView):

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        obj = get_object_or_404(queryset, pk=self.kwargs.get('id'), status='p')

        return obj

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.get_absolute_url() != self.request.path:
            return redirect(self.object, permanent=True)

        # See: super(PublicDetailView, self).get(request, *args, **kwargs)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

        # TODO: Find a way to call super() without retrieving the object twice
        # super(PublicDetailView, self).get(request, *args, **kwargs)
