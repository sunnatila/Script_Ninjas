from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    DEV_TYPE_CHOICES = (
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
    )

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    dev_type = models.CharField(max_length=15, choices=DEV_TYPE_CHOICES)
    test_count = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=55)
    message = models.TextField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name
