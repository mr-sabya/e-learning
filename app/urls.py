from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home, course

urlpatterns = [
    path('', home.Home, name="index"),

    path('course', course.Index, name="course.index"),
    path('course/<str:slug>', course.Show, name="course.show"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)