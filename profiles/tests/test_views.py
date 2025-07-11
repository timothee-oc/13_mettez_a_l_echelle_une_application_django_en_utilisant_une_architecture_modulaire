import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200
    assert b"Profiles" in response.content


@pytest.mark.django_db
def test_profile_view(client):
    user = User.objects.create(username='john_doe')
    Profile.objects.create(user=user, favorite_city='Paris')

    url = reverse('profiles:profile', args=['john_doe'])
    response = client.get(url)

    assert response.status_code == 200
    assert b"john_doe" in response.content
    assert b"Paris" in response.content
