from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('show', views.show),
    path('add',views.add),
    path("get/<str:id>",views.get)
]
