from django.urls import resolve, reverse
from lettings import views


def test_index_url_resolves():
    path = reverse('lettings:index')
    assert resolve(path).func == views.index
