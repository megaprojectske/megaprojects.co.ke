from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from articles.models import Article, Image

from .models import Program


class ProgramListedView(ListView):

    model = Program

    def get_queryset(self):
        # Check that status = True (Published)
        return Program.objects.published()


class ProgramArchiveView(ListView):

    model = Article
    paginate_by = 10
    template_name = 'programs/program_archive.html'

    def get_queryset(self):
        # Check that status = True (Published)
        self.program = get_object_or_404(
            Program, pk=self.kwargs.get('pk'), status=True)
        return Article.objects.published().filter(program=self.program)

    def get_context_data(self, **kwargs):
        context = super(ProgramArchiveView, self).get_context_data(**kwargs)
        context['program'] = self.program
        return context


class ProgramDetailView(DetailView):

    model = Program

    def get_queryset(self):
        # Check that status = True (Published)
        self.program = get_object_or_404(
            Program, pk=self.kwargs.get('pk'), status=True)
        return super(ProgramDetailView, self).get_queryset()


class ProgramCurrentView(DetailView):

    model = Program
    template_name = 'programs/program_current.html'

    def get_queryset(self):
        # Check that status = True (Published)
        self.program = get_object_or_404(
            Program, pk=self.kwargs.get('pk'), status=True)
        return super(ProgramCurrentView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super(ProgramCurrentView, self).get_context_data(**kwargs)
        context['article_list'] = [
            article for article in Article.objects.published().filter(program=self.object)[:12]]
        context['image_list'] = [image for image in Image.objects.published().filter(
            article__program=self.object)[:12]]

        popular_list = [article for article in Article.objects.published().filter(
            program=self.object)[:8]]

        # Only show popular list if more than 5 exist
        if len(popular_list) >= 5:
            context['popular_list'] = popular_list

        return context
