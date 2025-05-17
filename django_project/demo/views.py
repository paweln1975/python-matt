from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView, CreateView
from django_tables2 import SingleTableView

from demo.forms import PersonForm
from demo.models import Person
from demo.tables import PersonTable


def index_view(request):
    return redirect(reverse('demo-index-view'))

class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class PersonsList(SingleTableView):
    model = Person
    context_object_name = 'persons'
    template_name = 'person-list.html'
    table_class = PersonTable

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by('lastname', 'firstname')
        return data

class PersonDetailView(UpdateView):
    model = Person
    template_name = "person-detail.html"
    context_object_name = 'person'
    form_class = PersonForm

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class PersonUpdateView(PersonDetailView):
    template_name = 'person-update.html'

    def get_success_url(self):
        return reverse_lazy('demo-person-detail', kwargs={'pk': self.object.id})

class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('demo-person-list')
    context_object_name = 'person'
    template_name = 'person-delete.html'

class PersonCreateView(CreateView):
    model = Person
    template_name = "person-create.html"
    context_object_name = 'person'
    form_class = PersonForm

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('demo-person-detail', kwargs={'pk': self.object.id})