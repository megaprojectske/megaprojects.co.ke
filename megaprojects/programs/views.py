from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from articles.models import Article, Image

from core.views import PublicDetailView
from .models import Program


class ProgramListView(ListView):

    queryset = Program.objects.published()
    paginate_by = 6


class ProgramDetailView(DetailView):

    model = Program

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        url = reverse('program_detail', kwargs={
                      'id': self.object.id, 'slug': self.object.slug})

        if url != self.request.path:
            return redirect(url, permanent=True)

        # See: super(ProgramDetailView, self).get(request, *args, **kwargs)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        obj = get_object_or_404(
            queryset, pk=self.kwargs.get('id'), status=True)

        return obj


class ProgramArchiveView(ListView):

    model = Article
    paginate_by = 8
    template_name = 'programs/program_archive.html'

    def get(self, request, *args, **kwargs):
        self.program = get_object_or_404(
            Program, pk=self.kwargs.get('id'), status=True)
        url = reverse('program_archive', kwargs={
                      'id': self.program.id, 'slug': self.program.slug})

        if url != self.request.path:
            return redirect(url, permanent=True)

        return super(ProgramArchiveView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return Article.objects.published().filter(program=self.program)

    def get_context_data(self, **kwargs):
        context = super(ProgramArchiveView, self).get_context_data(**kwargs)
        context['program'] = self.program

        return context


class ProgramLatestView(PublicDetailView):

    model = Program
    template_name = 'programs/program_latest.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        obj = get_object_or_404(
            queryset, pk=self.kwargs.get('id'), status=True)

        return obj

    def get_context_data(self, **kwargs):
        context = super(ProgramLatestView, self).get_context_data(**kwargs)

        image_list = Image.objects.published().filter(
            article__program=self.object)[:12]
        image_list = [image for image in image_list]

        # Only show list if more than 5 exist
        if len(image_list) >= 5:
            context['image_list'] = image_list

        article_list = Article.objects.published().filter(
            program=self.object)[:11]
        context['article_list'] = [article for article in article_list]

        return context
