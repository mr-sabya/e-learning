from django.contrib import admin
from .models import Category, Services, ModuleCategory, Department, Instructor, Course, Course_module, Course_Software, Question_Answer

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


class Course_module(admin.TabularInline):
    model = Course_module

class Course_Software(admin.TabularInline):
    model = Course_Software

class Question_Answer(admin.TabularInline):
    model = Question_Answer


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = (Course_module, Course_Software, Question_Answer)



admin.site.register(Category, CategoryAdmin)
admin.site.register(ModuleCategory)
admin.site.register(Services)
admin.site.register(Department)
admin.site.register(Instructor)
admin.site.register(Course, CourseAdmin)
