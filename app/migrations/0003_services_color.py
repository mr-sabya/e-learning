# Generated by Django 4.2.1 on 2023-06-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='color',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
