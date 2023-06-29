from os import listdir
from os.path import isfile, join
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.


def file_list(request):
    onlyfiles = [
        f for f in listdir(settings.MEDIA_ROOT) if isfile(join(settings.MEDIA_ROOT, f))
    ]

    return render(
        request,
        "eos_files/file_list.html",
        context={"MEDIA_ROOT": settings.MEDIA_ROOT, "FILES": onlyfiles},
    )
