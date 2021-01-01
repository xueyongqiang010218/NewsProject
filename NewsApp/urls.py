from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('show/', views.Show, name='show'),
    path('add/', views.Add, name='add'),
    path('delete/<id>/', views.Delete, name='delete'),
]
