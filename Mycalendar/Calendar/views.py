import calendar
from datetime import datetime

from django.shortcuts import render

lst = [{'year': '1994', 'month' : '10', 'day' : '09'}]

def calendar(request):
    return render(request,'Calendar.html',{'data': lst})