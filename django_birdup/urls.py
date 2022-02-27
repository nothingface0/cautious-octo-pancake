from django.urls import path

from . import views

urlpatterns = [
    path('', views.birdup_home, name='birdup_home'),
]
