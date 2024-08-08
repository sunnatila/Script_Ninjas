from django.db import models
from django.utils.translation import gettext_lazy as _


class Science(models.Model):
    science_name = models.CharField(max_length=255, verbose_name="Fan nomi")
    tests = models.ManyToManyField(to='Test', verbose_name="Testlar")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.science_name


class Test(models.Model):
    question = models.CharField(max_length=255, verbose_name="Savol")
    question_image = models.ImageField(upload_to='question_images/', null=True, blank=True, verbose_name="Savol rasmi")
    variant1 = models.CharField(max_length=255, verbose_name="Variant 1")
    variant2 = models.CharField(max_length=255, verbose_name="Variant 2")
    variant3 = models.CharField(max_length=255, verbose_name="Variant 3")
    variant4 = models.CharField(max_length=255, verbose_name="Variant 4")
    right_answer = models.CharField(max_length=255, verbose_name="To`g`ri javob")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.question


class ExamTest(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Savol")
    selected_answer = models.CharField(max_length=255, verbose_name="Tanlangan javob")
    is_correct = models.BooleanField(default=False, verbose_name="To'g'ri javobmi")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    objects = models.Manager()

    def __str__(self):
        return self.user.username
