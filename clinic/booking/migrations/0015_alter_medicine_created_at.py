# Generated by Django 3.2.25 on 2024-07-12 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_medicine_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
