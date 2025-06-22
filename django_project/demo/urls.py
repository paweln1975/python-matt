from django.urls import path
from demo.views import IndexView, PersonsList, PersonUpdateView, PersonDeleteView, PersonDetailView, \
    PersonCreateView

app_name = 'demo'
urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('persons', PersonsList.as_view(), name='person-list' ),
    path('person/<int:pk>', PersonDetailView.as_view(), name='person-detail'),
    path('person/<int:pk>/update', PersonUpdateView.as_view(), name='person-update'),
    path('person/<int:pk>/delete', PersonDeleteView.as_view(), name='person-delete'),
    path('person/create', PersonCreateView.as_view(), name='person-create'),
]