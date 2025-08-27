from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model linked to the User model.
    Each user has one profile with a favorite city.
    Attributes:
    - user: OneToOneField to the User model.
    - favorite_city: CharField to store the user's favorite city.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        db_table = 'oc_lettings_site_profile'

    def __str__(self):
        return self.user.username
