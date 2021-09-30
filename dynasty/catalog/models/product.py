from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

User = get_user_model()

HTML_HELP_TXT = _("""Product description as content, color, uses cases.""")


class Product(models.Model):

    name = models.CharField(verbose_name=_(
        "Name"), max_length=150, unique=True, db_index=True)
    description = models.TextField(
        verbose_name=_("Description"), help_text=_(HTML_HELP_TXT), blank=True, null=True)
    image = models.ImageField(verbose_name=_(
        "Image"), upload_to="product_image/%Y/%m/%d", blank=True, null=True)
    price = models.FloatField(verbose_name=_(
        "Price"), help_text=_("Eg. 100.0"))
    points = models.PositiveIntegerField(
        verbose_name=_("Poins"), help_text=_("Eg. 14"))
    tax = models.FloatField(verbose_name=_("Tax (IVA)"),
                            help_text=_("Eg. 16"), null=True)
    status = models.BooleanField(verbose_name=_("Status"), default=False)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return self.name

    class Meta:
        app_label = "catalog"
        ordering = ("name", )
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def image_tag(self):
        if not self.image:
            return

        return format_html(
            '<img alt=\"{}\" src=\"{}\" width=\"75\" height=\"75\" styles=\"width: 100%;height: auto;\"/>',
            self.name,
            self.image.url,
        )

    image_tag.short_description = _("Image")
    image_tag.allow_tags = True
