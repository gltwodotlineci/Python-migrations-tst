from django.shortcuts import render
# from profiles.models import Profile, User


# def index(request):
#     """Render the users page."""
#     profiles = Profile.objects.all()
#     return render(request, 'profiles/index.html',
#                   {'profiles_list': profiles})


# def profile(request, username):
#     """ Render the user profile"""
#     profile = User.objects.get(username=username)
#     return render(request, 'profiles/profile.html', {'profile': profile})
