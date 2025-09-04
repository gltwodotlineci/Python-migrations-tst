from django.shortcuts import render
from profiles.models import Profile


def index(request):
    # x = 1.2 * "a"
    """
    Render the users page.
    Retrieves all Profile objects and renders the
    'profiles/index.html' template.

    Returns:
        HttpResponse: The rendered users page with all profiles.
    """
    profiles = Profile.objects.all()
    return render(request, 'profiles/index.html',
                  {'profiles_list': profiles})


def profile(request, username):
    """
    Render the user profile detail page.
    Retrieves the Profile object for the given username and renders the
    'profiles/profile.html' template.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is displayed.

    Returns:
        HttpResponse: The rendered profile detail page for the specified user.
    """
    profile = Profile.objects.get(user__username=username)
    return render(request, 'profiles/profile.html', {'profile': profile})
