from django_test.urls import urlpatterns


def global_context(request):
    """
    Global context processor
    """
    return {"urls": urlpatterns}
