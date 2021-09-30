import uuid

from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

from order.models import Status
from catalog.models import Product

User = get_user_model()


class Order(models.Model):

    order = models.CharField(verbose_name=_(
        "Order"), max_length=36, default=uuid.uuid4)
    partner = models.ForeignKey(User, verbose_name=_(
        "Partner"), null=True, blank=True, on_delete=models.SET_NULL)
    products = models.ForeignKey(Product, verbose_name=_(
        "Product"), related_name="products", on_delete=models.CASCADE)
    status = models.ForeignKey(Status, verbose_name=_(
        "Status"), on_delete=models.CASCADE)
    points = models.PositiveIntegerField(
        verbose_name=_("Poins"), help_text=_("Eg. 14"))
    subtotal = models.FloatField(
        verbose_name=_("Subtotal"), help_text=_("Eg. 100.0"))
    tax = models.FloatField(verbose_name=_("Tax (IVA)"),
                            help_text=_("Eg. 16.00"), null=True, default=0.00)
    grand_total = models.FloatField(
        verbose_name=_("Grand Total"), help_text=_("Eg. 100.0"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return self.order

    def save(self, *args, **kwargs):

        self.tax = (self.products.tax / 100) * self.grand_total
        self.points = self.grand_total / 100

        super(Order, self).save(*args, **kwargs)

    class Meta:
        app_label = "order"
        ordering = ("created_at", )
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
