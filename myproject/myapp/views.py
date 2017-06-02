from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import  Group

# Create your views here.

def get_Group(request):
    v = Group.objects.all()[0].name
    return HttpResponse(v)
