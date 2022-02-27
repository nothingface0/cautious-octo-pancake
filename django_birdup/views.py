from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def birdup_home(request):

    return render(request, template_name="django_birdup/birdup_home.html")
