from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from demo.models import Person

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class PersonsList(ListView):
    model = Person
    context_object_name = 'persons'
    template_name = 'persons.html'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by('lastname', 'firstname')
        return data
