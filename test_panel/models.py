from django.db import models


class TestModel(models.Model):
    question = models.CharField(max_length=255)
    question_image = models.ImageField(upload_to='question_images/', null=True, blank=True)
    variant1 = models.CharField(max_length=255)
    variant2 = models.CharField(max_length=255)
    variant3 = models.CharField(max_length=255)
    variant4 = models.CharField(max_length=255)
    right_answer = models.CharField(max_length=255)
    science = models.ManyToOneRel(to='Science', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.question


class Science(models.Model):
    science_name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.science_name


class ExamTest(models.Model):
    user = models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE)
    test_answer = models.ForeignKey(to=TestModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
