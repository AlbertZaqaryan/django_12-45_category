from django.shortcuts import render
from .models import Category
from django.db.models import Q
# Create your views here.

def index(request):
    search = request.GET.get('search')
    if search:
        category_list = Category.objects.filter(Q(name__icontains=search))
    else:
        category_list = Category.objects.all()
    return render(request, 'main/index.html', context={
        'category_list':category_list
    })

def prod(request, id):
    prod = Category.objects.filter(pk=id)
    return render(request, 'main/prod.html', context={
        'prod':prod
    })