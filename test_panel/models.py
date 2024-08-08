from django.db import models
from django.utils.translation import gettext_lazy as _


class Test(models.Model):
    question = models.CharField(max_length=255, verbose_name=_("Savol"))
    question_image = models.ImageField(upload_to='question_images/', null=True, blank=True, verbose_name=_("Savol rasmi"))
    variant1 = models.CharField(max_length=255, verbose_name=_("Variant 1"))
    variant2 = models.CharField(max_length=255, verbose_name=_("Variant 2"))
    variant3 = models.CharField(max_length=255, verbose_name=_("Variant 3"))
    variant4 = models.CharField(max_length=255, verbose_name=_("Variant 4"))
    right_answer = models.CharField(max_length=255, verbose_name=_("To`g`ri javob"))
    science = models.ForeignKey(to='Science', on_delete=models.CASCADE, verbose_name=_("Fan"))
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.question


class Science(models.Model):
    science_name = models.CharField(max_length=255, verbose_name=_("Fan nomi"))
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.science_name


class ExamTest(models.Model):
    user = models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    test_answer = models.ForeignKey(to=Test, on_delete=models.CASCADE, verbose_name=_("Savolning javobi"))
    status = models.CharField(max_length=255, verbose_name=_("Holati"))
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.user.username
