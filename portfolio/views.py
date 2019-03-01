from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def portfo(request):
    portfolios=Portfolio.objects
    return render(request,'portfo.html',{'portfolios':portfolios})