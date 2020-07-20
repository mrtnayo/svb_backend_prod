from django.contrib.auth import get_user_model
from django.db import models

from apps.common.models import Person, Ubigeo


User = get_user_model()


class Address(models.Model):
    HOME = 1
    OFFICE = 2
    OTHER = 0
    ADDRESS_CHOICES = (
        (HOME, 'Casa'),
        (OFFICE, 'Oficina'),
        (OTHER, 'Otros')
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    address_type = models.CharField(
        max_length=1,
        choices=ADDRESS_CHOICES,
        default=HOME
    )
    street_address = models.CharField(
        max_length=128
    )
    apartment_address = models.CharField(
        max_length=128,
        blank=True,
        null=True
    )
    ubigeo = models.ForeignKey(
        Ubigeo,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    zip = models.CharField(
        max_length=5
    )
    default = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class UserProfile(Person):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    billing_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
