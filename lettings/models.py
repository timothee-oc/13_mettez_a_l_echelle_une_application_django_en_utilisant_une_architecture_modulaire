"""
Models for the 'lettings' app.

This module defines the data structures related to property lettings,
including addresses and individual lettings.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address used in a letting.

    Attributes:
        number (PositiveIntegerField): Street number, max 4 digits.
        street (CharField): Name of the street (max 64 characters).
        city (CharField): City name (max 64 characters).
        state (CharField): State abbreviation (exactly 2 characters).
        zip_code (PositiveIntegerField): ZIP code, max 5 digits.
        country_iso_code (CharField): 3-letter ISO country code.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Return the number and the street of the address.
        """
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "addresses"


class Letting(models.Model):
    """
    Represents a property letting.

    Attributes:
        title (CharField): Title of the letting.
        address (OneToOneField): The associated address for the letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the title of the letting.
        """
        return self.title
