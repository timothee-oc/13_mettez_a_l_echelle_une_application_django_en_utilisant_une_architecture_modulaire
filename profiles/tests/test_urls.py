from django.urls import reverse, resolve
from profiles import views


def test_profiles_index_url_resolves():
    path = reverse('profiles:index')
    assert resolve(path).func == views.index


def test_profiles_detail_url_resolves():
    path = reverse('profiles:profile', args=['john_doe'])
    assert resolve(path).func == views.profile
