from django.urls import path
from . import views

urlpatterns = [
    path('', views.publications_list, name='publication_list'),
    path('add/', views.add_publication, name='add_publication'),
]
