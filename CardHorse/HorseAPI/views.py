from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def api_index(request):
    ###
    # This is the API Index page. It will contain instructions on how to access and use the Card Horse API.
    # This view does not do any processing, and should never do any processing, as it is public and anonymously-facing.
    ###
    return HttpResponse("Hello, world. This is the API Index.")
