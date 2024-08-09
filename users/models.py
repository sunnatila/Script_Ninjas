from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    DEV_TYPE_CHOICES = (
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
    )

    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefon raqam")
    dev_type = models.CharField(max_length=15, choices=DEV_TYPE_CHOICES, verbose_name="Ish Turi")

    def __str__(self):
        return self.username
