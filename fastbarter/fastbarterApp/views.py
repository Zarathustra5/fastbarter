from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Catalog
from django.views.generic import ListView

def index(request):
    return render(request, 'fastbarterApp/index.html')

def detail_catalog(request, catalog_id):
    detail_catalog = Catalog.objects.get(pk=catalog_id)
    return render(request, 'fastbarterApp/detail-catalog.html', {'detail_catalog': detail_catalog})

def catalog(request):
    # return HttpResponse('<h4>About</h4>')
    catalog = Catalog.objects.filter(is_published=True)
    return render(request, 'fastbarterApp/catalog.html', {'catalog': catalog})

def help(request):
    return render(request, 'fastbarterApp/help.html')

def new_product(request):
    return render(request, 'fastbarterApp/new-product.html')

def reviews(request):
    return render(request, 'fastbarterApp/reviews.html')

def account(request):
    return render(request, 'fastbarterApp/account/index.html')

def edit_profile(request):
    return render(request, 'fastbarterApp/account/edit-profile.html')

def favorite(request):
    catalog = Catalog.objects.filter(is_published=True, is_favorite=True)
    return render(request, 'fastbarterApp/favorite.html', {'catalog': catalog})

def services(request):
    return render(request, 'fastbarterApp/account/services.html')

def chats(request):
    return render(request, 'fastbarterApp/chats.html')
