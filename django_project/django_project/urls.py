"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demo.views import IndexView, index_view
from demo.views import PersonsList, PersonDetailView, PersonUpdateView, PersonDeleteView, PersonCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='default'),
    path('demo', IndexView.as_view(), name='demo-index-view'),
    path('demo/persons', PersonsList.as_view(), name='demo-person-list' ),
    path('demo/person/<int:pk>', PersonDetailView.as_view(), name='demo-person-detail'),
    path('demo/person/<int:pk>/update', PersonUpdateView.as_view(), name='demo-person-update'),
    path('demo/person/<int:pk>/delete', PersonDeleteView.as_view(), name='demo-person-delete'),
    path('demo/person/create', PersonCreateView.as_view(), name='demo-person-create'),
]

