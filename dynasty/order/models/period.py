from django.db import models
from django.utils.translation import gettext_lazy as _

from datetime import datetime, timedelta, date

dt = datetime.strptime(date.today().strftime("%d/%b/%Y"), '%d/%b/%Y')
start = dt - timedelta(days=dt.weekday())
end = start + timedelta(days=6)


class Period(models.Model):

    period = models.CharField(max_length=100, null=True)
    start = models.DateTimeField(
        _("Start"), default=start)
    end = models.DateTimeField(
        _("End"), default=end)
    complete = models.DateTimeField(
        _("Complete Date"), null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return self.period

    class Meta:
        app_label = "order"
        ordering = ("created_at", )
        verbose_name = _("Period")
        verbose_name_plural = _("Periods")
