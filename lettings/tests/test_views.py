import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200
    assert b"Lettings" in response.content


@pytest.mark.django_db
def test_letting_view(client):
    address = Address.objects.create(
        number=5, street="Rue Bleue", city="Nice", state="FR",
        zip_code=6000, country_iso_code="FRA"
    )
    letting = Letting.objects.create(title="Villa", address=address)
    response = client.get(reverse('lettings:letting', args=[letting.id]))
    assert response.status_code == 200
    assert b"Villa" in response.content
