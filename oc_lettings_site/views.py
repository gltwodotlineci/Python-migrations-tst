from django.shortcuts import render
# from django.conf.urls import handler404


def home(request):
    """
    Render the index page of lettings.
    """
    return render(request, 'home.html')


def views_404(request, exception):
    """
    Render the 404 page.
    """
    return render(request, 'profiles/404.html')


# handler404 = views_404

# if handler404:
#     print("handler404 is set")
