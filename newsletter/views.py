from django.views.generic import TemplateView
from utils.database_routers import read_replica_or_default

from newsletter.models import Article, Newsletter, Reporter


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['articles'] = Article.objects.using(read_replica_or_default()).all()
        # context['articles'] = Article.objects.using('default').all()
        context['reporters'] = Reporter.objects.all()
        context['newsletter'] = Newsletter.objects.all()

        return context
