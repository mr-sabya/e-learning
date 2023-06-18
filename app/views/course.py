from django.shortcuts import render
from django.http import HttpResponse
from ..models import Category, Course

def Index(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'course/index.html', context)


def Show(request, slug):
    course = Course.objects.get(slug = slug)

    context = {
        'course' : course
    }

    return render(request, 'course/show.html', context)