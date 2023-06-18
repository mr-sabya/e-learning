from django.shortcuts import render
from django.http import HttpResponse
from ..models import Category, Services

def Home(request):
    categories = Category.objects.all()
    services = Services.objects.all()
    course_categories = Category.objects.all()[:2]

    context = {
        'categories': categories,
        'services': services,
        'course_categories': course_categories
    }
    return render(request, 'home/index.html', context)