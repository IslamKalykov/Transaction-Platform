from django.db import models
from django.utils.translation import gettext_lazy as _


class Transaction(models.Model):
    class Status(models.TextChoices):
        RECEIVED = "received", "received"
        PROCESSING = "processing", "processing"
        CANCEL = "cancel", "cancel"

    from_account = models.ForeignKey('account.Account', on_delete=models.CASCADE, related_name='transactions_sent')
    to_account = models.ForeignKey('account.Account', on_delete=models.CASCADE, related_name='transactions_recieved')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=40, choices=Status.choices, default=Status.PROCESSING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("transaction")
        verbose_name_plural = _("transactions")

    def __str__(self):
        return f'{self.from_account.phone} to {self.to_account.phone}'
