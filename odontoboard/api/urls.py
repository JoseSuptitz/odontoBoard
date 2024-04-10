from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_pacient, name='Add'),
    path('pacients/', views.view_pacients, name='all_pacients'),
    path('update/<int:pk>/', views.update_pacients, name='Update'),
    path('delete/<int:pk>/', views.delete_pacients, name="Delete"),
]