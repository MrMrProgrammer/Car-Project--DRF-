from django.urls import path, include
from . import views

urlpatterns = [
    path('show', views.show),
    path('add', views.add),
    path('update', views.update),
    path('delete', views.delete),
]
