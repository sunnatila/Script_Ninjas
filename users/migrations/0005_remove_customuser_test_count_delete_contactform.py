# Generated by Django 5.0.8 on 2024-08-08 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='test_count',
        ),
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]
