from .models import Test, Science, ExamTest
from django.contrib import admin


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('question', 'right_answer', 'science')


@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ('science_name',)


@admin.register(ExamTest)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('user',)
