from .models import Test, Science, ExamTest
from django.contrib import admin


@admin.register(Test)
class BankAdmin(admin.ModelAdmin):
    list_display = ('question', 'right_answer', 'science')


@admin.register(Science)
class TestAdmin(admin.ModelAdmin):
    list_display = ('science_name',)


@admin.register(ExamTest)
class TestAdmin(admin.ModelAdmin):
    list_display = ('status',)
