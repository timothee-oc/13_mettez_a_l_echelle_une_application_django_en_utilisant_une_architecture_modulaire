"""
Views for the 'profiles' app.

This module provides views to list all user profiles and display details
for a specific profile based on the username.
"""
from django.shortcuts import render

from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def index(request):
    """
    View function for the profiles index page.

    Retrieves all profiles from the database and renders them
    in the 'profiles/index.html' template.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML page displaying the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis, pellentesque
# dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis fringilla, eros leo
# tristique lacus, it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique
# senectus et netus et males
def profile(request, username):
    """
    View function for an individual profile detail page.

    Retrieves a profile based on the associated user's username
    and renders it in the 'profiles/profile.html' template.

    Args:
        request (HttpRequest): The incoming HTTP request.
        username (str): The username of the profile to retrieve.

    Returns:
        HttpResponse: Rendered HTML page displaying profile details.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
