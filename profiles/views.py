from django.shortcuts import render
from profiles.models import Profile


def index(request):
    # x = 1.2 * "a"
    """
    Render the users page.
    """
    profiles = Profile.objects.all()
    return render(request, 'profiles/index.html',
                  {'profiles_list': profiles})


def profile(request, username):
    """
    Render the user profile detail page. 
    """
    profile = Profile.objects.get(user__username=username)
    return render(request, 'profiles/profile.html', {'profile': profile})
