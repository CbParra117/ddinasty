from django.db import models
from django.utils.translation import ugettext_lazy as _

from .user import User

# Create your models here.


class Address(models.Model):

    user = models.ForeignKey(
        User,
        related_name='user_address',
        on_delete=models.CASCADE)
    street = models.CharField(
        verbose_name=_('Street'),
        max_length=255,
        blank=True)
    external_number = models.CharField(
        verbose_name=_('External Number'),
        max_length=120,
        blank=True)
    inside_number = models.CharField(
        verbose_name=_('Inside Number'),
        max_length=100,
        blank=True,
        null=True)
    postcode = models.CharField(
        verbose_name=_('Zip'),
        max_length=8,
        blank=True,
        db_index=True)
    colony = models.CharField(
        verbose_name=_('Colony'),
        max_length=255,
        blank=True,
        null=True)
    municipality = models.CharField(
        verbose_name=_('Municipality'),
        max_length=255,
        blank=True,
        null=True)
    city = models.CharField(
        verbose_name=_('City'),
        max_length=255,
        blank=True,
        null=True)
    state_province = models.CharField(
        verbose_name=_('State / Province'),
        max_length=255,
        blank=True,
        null=True)
    country = models.CharField(
        verbose_name=_('country'),
        max_length=255,
        blank=True,
        null=True)
    created_at = models.DateTimeField(
        verbose_name=_('Created At'),
        auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name=_('Updated At'),
        auto_now=True)

    def __str__(self):
        return self.street

    class Meta:
        app_label = "users"
        verbose_name = _('address')
        verbose_name_plural = _('address')
