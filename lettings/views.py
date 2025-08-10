from django.shortcuts import render
# from lettings.models import Letting

# def index(request):
#     """
#     Render the index page of profiles.
#     """
#     lettings = Letting.objects.all()

#     return render(request, 'lettings/index.html',
#                   {'lettings_list': lettings})


# def letting(request,letting_id):
#     letting = Letting.objects.get(id=letting_id)
#     title = letting.title
#     address = letting.address
#     context = {
#         'title': title,
#         'address': address,
#     }
#     return render(request, 'lettings/letting.html', context=context)
