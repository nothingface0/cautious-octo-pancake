from django_tables2 import SingleTableView
from django.views.generic import ListView
from .models import Person
from .tables import PersonTable


class PersonListView(SingleTableView):
    model = Person
    template_name = 'tutorial/people.html'
    table_class = PersonTable
