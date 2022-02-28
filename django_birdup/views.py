from os import listdir, sep
from os.path import isfile, join
from django.shortcuts import render
from django.http import HttpResponse
import logging


# Create your views here.
def birdup_home(request):

    logging.info("!!!!")
    # Test reading listing files from EOS
    rootpath = join(sep, 'eos', 'user', 'b', 'birdup', 'test')
    logging.info(listdir(rootpath))

    return render(request, template_name="django_birdup/birdup_home.html")
