from django.db import models


class Bank(models.Model):
    bank_name = models.CharField(max_length=255)
    bank_info = models.TextField()
    bank_location = models.CharField(max_length=255, null=True, blank=True)
    bank_image = models.ImageField(upload_to='bank_images/', null=True, blank=True)
    bank_phone = models.CharField(max_length=255, null=True, blank=True)
    bank_email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.bank_name
