# Generated by Django 4.2.1 on 2023-06-18 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_department_instructor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('tagline', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('total_class', models.IntegerField()),
                ('project', models.IntegerField()),
                ('image', models.ImageField(upload_to='media/course')),
                ('short_description', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('price', models.IntegerField()),
                ('offline_price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('instructors', models.ManyToManyField(to='app.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Question_Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/software')),
                ('title', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Course_module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('module', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
        ),
    ]
