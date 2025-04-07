# projects/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('add/', views.add_project, name='add_project'),  # For the extra challenge
    path('update-project-images/', views.update_project_images, name='update_project_images'),
]