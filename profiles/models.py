"""
Models for the 'profiles' app.

Defines user profile extensions, allowing the association of a favorite city
with each Django-authenticated user.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Extends the built-in Django User model with additional profile information.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the Django User.
        favorite_city (CharField): Optional favorite city for the user (max 64 characters).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return the username of the associated user as string representation.
        """
        return self.user.username
