from django.shortcuts import render


def index(request):
    """
    Render the index page of profiles.
    """
    return render(request, 'lettings/index.html')
