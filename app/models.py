from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='media/category')


    def __str__(self):
        return self.name
    


class Services(models.Model):
    title = models.CharField(max_length=80)
    icon = models.ImageField(upload_to='media/services')
    service = models.TextField(max_length=255)
    color = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.title
    


class ModuleCategory(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    


class Department(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    intro = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/instructors')
    description = models.TextField()
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.name
    

class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=255)
    duration = models.FloatField()
    total_class = models.IntegerField()
    project = models.IntegerField()
    image = models.ImageField(upload_to='media/course')
    short_description = RichTextField()
    overview = RichTextField()
    price = models.IntegerField()
    offline_price = models.IntegerField()
    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return self.title
    

class Course_module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    module = RichTextField()


class Course_Software(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/software')
    title = models.CharField(max_length=100)

class Question_Answer(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

