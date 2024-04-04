from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    team = Team.objects.all()
    return render(request, 'index.html', {'key': obj, 'team': team})


# def about(request):
#     return render(request, 'about.html')
#
#
# def contact(request):
#     return render(request, 'contact.html')
#
#
# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res = x + y
#     return render(request, "addition.html", {'key': res, 'num1': x, 'num2': y})
