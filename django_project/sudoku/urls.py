from django.urls import path
from . import views

app_name = 'sudoku'
urlpatterns = [
    path('', views.puzzle_list, name='puzzle_list'),
    path('puzzle/<int:pk>/', views.puzzle_detail, name='puzzle_detail'),
    path('puzzle/new/', views.puzzle_create, name='puzzle_create'),
    path('puzzle/<int:pk>/solve/', views.puzzle_solve, name='puzzle_solve'),
    path('puzzle/<int:pk>/edit/', views.puzzle_edit, name='puzzle_edit'),
    path('puzzle/<int:pk>/delete/', views.puzzle_delete, name='puzzle_delete'),
    path('puzzle/<int:pk>/generate-solution/', views.puzzle_generate_solution, name='puzzle_generate_solution'),

]