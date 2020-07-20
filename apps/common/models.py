from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from softdelete.models import SoftDeleteModel


User = get_user_model()


class TimeStampedModel(models.Model):
    """
    Modelo abstracto que implementa los campos de seguimiento
    de cambios al modelo.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OwnedModel(models.Model):
    """
    Modelo abstracto que implementa el campo owner(propietario) del recurso.
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_('Usuario propietario del recurso')
    )

    class Meta:
        abstract = True


class Person(TimeStampedModel, SoftDeleteModel):
    """
    Modelo abstracto que encapsula toda la información de una persona.
    """
    DOCUMENT_TYPE_OTR = '00'
    DOCUMENT_TYPE_DNI = '01'
    DOCUMENT_TYPE_EXT = '04'
    DOCUMENT_TYPE_RUC = '06'
    DOCUMENT_TYPE_PSS = '07'
    DOCUMENT_TYPE_PNC = '11'
    DOCUMENT_TYPE_CHOICES = (
        (DOCUMENT_TYPE_OTR, 'OTROS'),
        (DOCUMENT_TYPE_DNI, 'L.E. / DNI'),
        (DOCUMENT_TYPE_EXT, 'CARNET EXT.'),
        (DOCUMENT_TYPE_RUC, 'RUC'),
        (DOCUMENT_TYPE_PSS, 'PASAPORTE'),
        (DOCUMENT_TYPE_PNC, 'P. NAC.')
    )
    document_type = models.CharField(
        _('Document Type'),
        max_length=2,
        choices=DOCUMENT_TYPE_CHOICES,
        default=DOCUMENT_TYPE_DNI,
        blank=True,
        null=True,
        help_text=_('Tipo de documento')
    )
    document_number = models.CharField(
        _('Document Number'),
        max_length=15,
        blank=True,
        null=True,
        help_text=_('Número de documento')
    )
    first_name = models.CharField(
        _('First Name'),
        max_length=50,
        blank=True,
        null=True,
        help_text=_('Nombres')
    )
    last_name = models.CharField(
        _('Last Name'),
        max_length=50,
        blank=True,
        null=True,
        help_text=_('Apellidos')
    )
    birthdate = models.DateField(
        _('Birthdate'),
        blank=True,
        null=True,
        help_text=_('Fecha de nacimiento')
    )
    mobile_phone_number = models.CharField(
        _('Mobile phone number'),
        max_length=15,
        blank=True,
        null=True,
        help_text=_('Número de celular')
    )
    home_phone_number = models.CharField(
        _('Home phone number'),
        max_length=15,
        blank=True,
        null=True,
        help_text=_('Número de teléfono casa')
    )
    work_phone_number = models.CharField(
        _('Work phone number'),
        max_length=15,
        blank=True,
        null=True,
        help_text=_('Número de oficina o centro de trabajo')
    )
    nationality = models.CharField(
        _('Nationality'),
        max_length=30,
        blank=True,
        null=True,
        help_text=_('Nacionalidad')
    )

    class Meta:
        abstract = True
        unique_together = ('document_type', 'document_number')

    def __str__(self):
        return '{} {}'.format(self.document_number, self.last_name)

    def get_full_name(self, separator=' ', order=None):
        if order == 'first':
            return '{}{}{}'.format(self.first_name, separator, self.last_name)
        return '{}{}{}'.format(self.last_name, separator, self.first_name)

    @property
    def age(self):
        return relativedelta(timezone.now().date(), self.birthdate)


class Ubigeo(models.Model):
    """
    Modelo que maneja la información de ubigeo
    """
    code = models.CharField(
        _('Code'),
        max_length=6,
        primary_key=True,
        help_text=_('Código de ubigeo')
    )
    department = models.CharField(
        _('Department'),
        max_length=30,
        help_text=_('Departamento')
    )
    province = models.CharField(
        _('Province'),
        max_length=30
    )
    district = models.CharField(
        _('District'),
        max_length=30,
        help_text=_('Distrito')
    )

    class Meta:
        ordering = (
            'department',
            'province',
            'district'
        )

    def __str__(self):
        return '{} - {} - {}'.format(
            self.department, self.province, self.district
        )
