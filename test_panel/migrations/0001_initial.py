# Generated by Django 5.0.8 on 2024-08-08 04:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('science_name', models.CharField(max_length=255, verbose_name='Fan nomi')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Savol')),
                ('question_image', models.ImageField(blank=True, null=True, upload_to='question_images/', verbose_name='Savol rasmi')),
                ('variant1', models.CharField(max_length=255, verbose_name='Variant 1')),
                ('variant2', models.CharField(max_length=255, verbose_name='Variant 2')),
                ('variant3', models.CharField(max_length=255, verbose_name='Variant 3')),
                ('variant4', models.CharField(max_length=255, verbose_name='Variant 4')),
                ('right_answer', models.CharField(max_length=255, verbose_name='To`g`ri javob')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('science', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_panel.science', verbose_name='Fan')),
            ],
        ),
        migrations.CreateModel(
            name='ExamTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255, verbose_name='Holati')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
                ('test_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_panel.test', verbose_name='Savolning javobi')),
            ],
        ),
    ]