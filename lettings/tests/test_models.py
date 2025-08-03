import pytest
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_str():
    assert False
    address = Address.objects.create(
        number=10,
        street="Rue de Paris",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA"
    )
    assert str(address) == "10 Rue de Paris"


@pytest.mark.django_db
def test_letting_str():
    address = Address.objects.create(
        number=42,
        street="Rue Victor Hugo",
        city="Lyon",
        state="FR",
        zip_code=69000,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(title="Appartement centre-ville", address=address)
    assert str(letting) == "Appartement centre-ville"
