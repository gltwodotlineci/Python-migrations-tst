from django.shortcuts import render


def home(request):
    """
    Render the index page of lettings.
    """
    return render(request, 'home.html')
