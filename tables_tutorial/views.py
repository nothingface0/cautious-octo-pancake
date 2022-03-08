from django.shortcuts import render
from django.views.generic import ListView
from .models import Person


class PersonListView(ListView):
    model = Person
    template_name = 'tutorial/people.html'
