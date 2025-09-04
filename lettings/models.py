from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model for creating an Address object.

    Attributes:
        number (int): The street number.
        street (str): The street name.
        city (str): The city name.
        state (str): The state or province.
        zip_code (int): The postal code.
        country_iso_code (str): The ISO code of the country.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        db_table = 'oc_lettings_site_address'
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Model for creating a Letting object.

    Attributes:
        title (str): The title of the letting.
        address (Address): The associated Address object.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = 'oc_lettings_site_letting'

    def __str__(self):
        return self.title
