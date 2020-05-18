from django.shortcuts import render

# Create your views here.

'view that shows splash page'


def splash(request):

    return render(request, "splash.html", {})