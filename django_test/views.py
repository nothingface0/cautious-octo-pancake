import logging
from django.shortcuts import render


def home(request):
    return render(request, 'django_test/base.html')
