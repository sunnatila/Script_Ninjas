from django.db import models
from django.utils.translation import gettext_lazy as _


class Bank(models.Model):
    bank_name = models.CharField(max_length=255, verbose_name=_("Bank nomi"))
    bank_info = models.TextField(verbose_name=_("Bank haqida"))
    bank_location = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Bank manzili"))
    bank_image = models.ImageField(upload_to='bank_images/', null=True, blank=True, verbose_name=_("Bank rasmi"))
    bank_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Bank telefon raqami"))
    bank_email = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Bank emaili"))
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.bank_name

    objects = models.Manager()
