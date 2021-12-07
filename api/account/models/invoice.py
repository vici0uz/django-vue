from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import BaseModel


# Create your models here.
class AccountInvoice(BaseModel):

    date = models.DateField(_("Invoice Date"), auto_now=False, auto_now_add=False)


class AccountInvoiceLine(BaseModel):

    invoice = models.ForeignKey("account.AccountInvoice", verbose_name=_("Invoice"), on_delete=models.RESTRICT)