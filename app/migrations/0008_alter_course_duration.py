# Generated by Django 4.2.1 on 2023-06-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_course_question_answer_course_software_course_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.FloatField(),
        ),
    ]