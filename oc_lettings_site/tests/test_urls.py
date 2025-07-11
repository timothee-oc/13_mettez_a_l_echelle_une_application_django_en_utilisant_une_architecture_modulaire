from django.urls import reverse, resolve
from oc_lettings_site import views as site_views
from lettings import views as lettings_views
from profiles import views as profiles_views


def test_root_url_resolves_to_index_view():
    path = reverse('index')
    resolved_view = resolve(path)
    assert resolved_view.func == site_views.index


def test_raise_500_url_resolves():
    path = reverse('raise_500')
    resolved_view = resolve(path)
    assert resolved_view.func == site_views.raise_500


def test_lettings_namespace_index():
    url = reverse('lettings:index')
    assert url.startswith('/lettings/')
    resolved_view = resolve(url)
    assert resolved_view.func == lettings_views.index


def test_profiles_namespace_index():
    url = reverse('profiles:index')
    assert url.startswith('/profiles/')
    resolved_view = resolve(url)
    assert resolved_view.func == profiles_views.index
