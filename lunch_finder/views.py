from django.views import generic
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'lunch_finder/index.html'
    title = "Index"
