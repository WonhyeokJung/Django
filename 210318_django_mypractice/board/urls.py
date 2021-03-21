from django.contrib import admin
from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    # C
    path('new/', views.new, name='new'),
    # R
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name= 'detail'),
    # U
    path('<int:pk>/edit/', views.edit, name= 'edit'),
    # D
    path('<int:pk>/delete/', views.delete, name = 'delete'),
]
