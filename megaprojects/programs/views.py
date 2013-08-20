from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from articles.models import Article, Image

from core.views import PublicDetailView
from .models import Program


class ProgramListView(ListView):

    # Check that status = 'p' (Published)
    queryset = Program.objects.published()
    paginate_by = 6


class ProgramArchiveView(ListView):

    model = Article
    paginate_by = 8
    template_name = 'programs/program_archive.html'

    def get_queryset(self):
        # Check that status = True (Published)
        self.program = get_object_or_404(
            Program, pk=self.kwargs.get('id'), status=True)

        return Article.objects.published().filter(program=self.program)

    def get_context_data(self, **kwargs):
        context = super(ProgramArchiveView, self).get_context_data(**kwargs)
        context['program'] = self.program

        return context


class ProgramDetailView(DetailView):

    model = Program

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        # Check that status = True (Published)
        obj = get_object_or_404(
            queryset, pk=self.kwargs.get('id'), status=True)

        return obj


class ProgramLatestView(PublicDetailView):

    model = Program
    template_name = 'programs/program_latest.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        # Check that status = True (Published)
        obj = get_object_or_404(
            queryset, pk=self.kwargs.get('id'), status=True)

        return obj

    def get_context_data(self, **kwargs):
        context = super(ProgramLatestView, self).get_context_data(**kwargs)

        popular_list = [article for article in Article.objects.published().filter(
            program=self.object)[:8]]
        image_list = [image for image in Image.objects.published().filter(
            article__program=self.object)[:12]]

        context['article_list'] = [
            article for article in Article.objects.published().filter(program=self.object)[:11]]

        # Only show list if more than 5 exist
        if len(popular_list) >= 5:
            context['popular_list'] = popular_list
        if len(image_list) >= 5:
            context['image_list'] = image_list

        return context
