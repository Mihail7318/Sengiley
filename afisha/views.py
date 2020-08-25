from django.shortcuts import render
from .models import afisha, holiday
from datetime import datetime
# Create your views here.

def afisha_detail(request):
    date_n = datetime.now().date()
    films = afisha.objects.filter(date_out__gte = date_n)
    return render(request, "afisha-s.html", {'films': films})

def holiday_detail(request, pk):
    hol = holiday.objects.filter(id = pk)
    return render(request, "holiday.html", {'hol': hol})

