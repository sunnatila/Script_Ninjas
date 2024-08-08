# Generated by Django 5.0.8 on 2024-08-08 04:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_dev_type_customuser_test_count'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='dev_type',
            field=models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend')], max_length=15, verbose_name='Ish Turi'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefon raqam'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='test_count',
            field=models.IntegerField(default=0, verbose_name='Test yechish uchun urunish'),
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=55, verbose_name='Telefon raqam')),
                ('message', models.TextField(verbose_name='Xabar')),
                ('status', models.CharField(max_length=100, verbose_name='Holati')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
        ),
    ]
