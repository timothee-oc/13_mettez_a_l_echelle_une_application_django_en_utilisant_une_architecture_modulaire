"""
Views for the main app

Essentially the index view, that is the main entry point of the site.
Any other views that are not related to a specific app.
"""

from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi
# convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus. Aliquam vitae erat
# ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    View function for the main index page.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML page displaying the list of lettings.
    """
    return render(request, 'index.html')


def raise_500(request):
    """
    Just a little helping view to test the custom 500 error page.
    """
    raise Exception("ERREUR 500")
