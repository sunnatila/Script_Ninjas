from django.db import models


class Bank(models.Model):
    bank_name = models.CharField(max_length=255, verbose_name="Bank nomi")
    bank_info = models.TextField(verbose_name="Bank haqida")
    bank_location = models.CharField(max_length=255, null=True, blank=True, verbose_name="Bank manzili")
    bank_image = models.ImageField(upload_to='bank_images/', null=True, blank=True, verbose_name="Bank rasmi")
    bank_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name="Bank telefon raqami")
    bank_email = models.CharField(max_length=255, null=True, blank=True, verbose_name="Bank emaili")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.bank_name

