from django.shortcuts import render


def indexabc(request):
    """Render the user profile page."""
    return render(request, 'profiles/index.html')
