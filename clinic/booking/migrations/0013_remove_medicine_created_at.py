# Generated by Django 3.2.25 on 2024-07-12 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_remove_medicine_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='created_at',
        ),
    ]
