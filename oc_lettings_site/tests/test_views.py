import pytest
from django.urls import reverse
from django.test import Client


def test_index_view():
    client = Client()
    url = reverse('index')
    response = client.get(url)

    assert response.status_code == 200
    assert b'<title>' in response.content


def test_raise_500_view(client):
    url = reverse('raise_500')

    with pytest.raises(Exception) as exc_info:
        client.get(url)

    assert str(exc_info.value) == "ERREUR 500"
