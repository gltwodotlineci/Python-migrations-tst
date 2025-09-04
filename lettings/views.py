from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """
    Render the index page of profiles.

    Returns:
        HttpResponse: The rendered index page with all lettings.
    """
    lettings = Letting.objects.all()

    return render(request, 'lettings/index.html',
                  {'lettings_list': lettings})


def letting(request, letting_id):
    """
    Render the detail page for a specific letting.
    Retrieves the Letting object with the given ID and renders the
    'lettings/letting.html' template with its title and address.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: The rendered letting detail page for the specified letting.
    """
    letting = Letting.objects.get(id=letting_id)
    title = letting.title
    address = letting.address
    context = {
        'title': title,
        'address': address,
    }
    return render(request, 'lettings/letting.html', context=context)
