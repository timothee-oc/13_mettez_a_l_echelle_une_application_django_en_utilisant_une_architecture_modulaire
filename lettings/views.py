"""
Views for the 'lettings' app.

This module handles the display of all lettings as well as
the detail page for a specific letting.
"""

from django.http import Http404
from django.shortcuts import render

from .models import Letting

import logging

logger = logging.getLogger(__name__)


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu. Vestibulum ante ipsum primis in
# faucibus orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    View function for the lettings index page.

    Retrieves all lettings from the database and renders them
    in the 'lettings/index.html' template.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML page displaying the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae
# efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est
# ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse
# potenti. In tempus a nisi sed laoreet. Suspendisse porta dui eget sem accumsan interdum. Ut quis
# urna pellentesque justo mattis ullamcorper ac non tellus. In tristique mauris eu velit
# fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero, eget bibendum lorem.
# Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer
# vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    View function for an individual letting detail page.

    Retrieves the letting by its ID and renders the
    'lettings/letting.html' template with title and address.

    Args:
        request (HttpRequest): The incoming HTTP request.
        letting_id (int): The ID of the letting to retrieve.

    Returns:
        HttpResponse: Rendered HTML page displaying letting details.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.error(f"Lettings not found for id {letting_id}")
        raise Http404
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
