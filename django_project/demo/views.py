from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from demo.models import Person
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args, **kwargs)

class PersonsList(ListView):
    model = Person
    context_object_name = 'persons'
    template_name = 'persons.html'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by('lastname', 'firstname')
        return data

class PersonDetailView(DetailView):
    model = Person
    template_name = "person-detail.html"
    context_object_name = 'person'

    def dispatch(self, request, *args, **kwargs):
        print(request.user, request.user.is_authenticated)
        return super().dispatch(request,*args, **kwargs)

class PersonCreateView(CreateView):
    model = Person
    template_name = "person-create.html"
    fields = '__all__'

class PersonUpdateView(UpdateView):
    model = Person
    fields = ['lastname', 'firstname']
    template_name = 'person_update_form.html'

class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('demo-persons-list')
    template_name = 'person-confirm-delete.html'

