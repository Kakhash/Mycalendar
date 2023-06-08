
from django.contrib import admin
from django.urls import path
from Calendar.views import calendar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Calendar',calendar,name="calendar")
]
