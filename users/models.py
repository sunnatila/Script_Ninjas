from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    DEV_TYPE_CHOICES = (
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
    )

    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name=_("Telefon raqam"))
    dev_type = models.CharField(max_length=15, choices=DEV_TYPE_CHOICES, verbose_name=_("Ish Turi"))
    test_count = models.IntegerField(default=0, verbose_name=_("Test yechish uchun urunish"))

    objects = models.Manager()

    def __str__(self):
        return self.username


class ContactForm(models.Model):
    name = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, verbose_name=_("Username"))
    phone = models.CharField(max_length=55, verbose_name=_("Telefon raqam"))
    message = models.TextField(verbose_name=_("Xabar"))
    status = models.CharField(max_length=100, verbose_name=_("Holati"))

    objects = models.Manager()

    def __str__(self):
        return self.name

