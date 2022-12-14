from django.shortcuts import render
from django.views.generic import ListView
from .models import Test

# Create your views here.
class TestView(ListView):
    model = Test
    template_name = 'test.html'