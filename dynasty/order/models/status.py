from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):

    name = models.CharField(verbose_name=_(
        "Name"), max_length=150, unique=True, db_index=True)
    description = models.TextField(
        verbose_name=_("Description"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return self.name

    class Meta:
        app_label = "order"
        ordering = ("created_at", )
        verbose_name = _("Status")
        verbose_name_plural = _("Status")
