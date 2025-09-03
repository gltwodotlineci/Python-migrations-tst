from django.shortcuts import render


def home(request):
    """
    Render the index page of lettings.
    """
    return render(request, 'home.html')


def views_404(request, exception):
    """
    Render the 404 page.
    """
    return render(request, "errors/404.html", status=404)


def views_500(request):
    """
    Render the 500 error page.
    """
    return render(request, "errors/500.html", status=500)
