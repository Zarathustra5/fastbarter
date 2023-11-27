from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Catalog
from .models import Groups
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def index(request):
    return render(request, 'fastbarterApp/index.html')

def detail_catalog(request, catalog_id):
    detail_catalog = Catalog.objects.get(pk=catalog_id)
    favorite = ""

    if request.user.is_authenticated & (request.method == "POST"):
        favorite = Favorite.objects.filter(user=request.user)
        if request.POST["remove_favorite"]:
            Favorite.objects.filter(user=request.user, catalog_id=catalog_id).delete()
        else:
            Favorite.objects.create(user=request.user, catalog_id=catalog_id)

    return render(request, 'fastbarterApp/detail-catalog.html', {'detail_catalog': detail_catalog, "favorite": favorite})

def catalog(request):
    # return HttpResponse('<h4>About</h4>')
    search = request.GET.get("s")
    catalog = Catalog.objects.filter(is_published=True)
    favorite = ""
    form = ""

    if (request.method == "POST") & (not request.user.is_authenticated):
        return redirect('/account/login')

    if request.user.is_authenticated:
        favorite = Favorite.objects.filter(user=request.user)
        if request.method == "POST":
            if request.POST["remove_favorite"]:
                Favorite.objects.filter(user=request.user, catalog_id=request.POST["remove_favorite"]).delete()
                form = FavoriteForm()
            else:
                form = FavoriteForm(request.POST)
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                #form.save()

        else:
            form = FavoriteForm()

    return render(request, 'fastbarterApp/catalog.html', {'catalog': catalog, 'search': search, "form": form, "favorite": favorite})

def catalog_login(request):
    catalog = Catalog.objects.filter(is_published=True)
    return render(request, 'fastbarterApp/login.html', {'catalog': catalog})

def help(request):
    return render(request, 'fastbarterApp/help.html')

@login_required
def new_product(request):
    success = False
    if request.method == "POST":
        form = NewProductForm(request.POST, request.FILES)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        #form.save()
        success = True

    else:
        form = NewProductForm()

    return render(request, 'fastbarterApp/new-product.html', {"form": form, "success": success})

def reviews(request):
    return render(request, 'fastbarterApp/reviews.html')

@login_required
def my_reviews(request):
    return render(request, 'fastbarterApp/account/my-reviews.html')

@login_required
def account(request):
    catalog = Catalog.objects.filter(user=request.user)
    return render(request, 'fastbarterApp/account/index.html', {'catalog': catalog})

@login_required
def edit_profile(request):
    if request.method == "POST":
        #form = EditProfileForm(request.POST)
        #CustomUsers.objects.filter(pk=request.user.id).update(name=request.POST["name"], phone_number=request.POST["phone_number"])
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        form.save()

    else:
        form = EditProfileForm(initial={'name': request.user.name, 'phone_number': request.user.phone_number, 'email': request.user.email })

    return render(request, "fastbarterApp/account/edit-profile.html", {"form": form})

@login_required
def settings(request):
    return render(request, 'fastbarterApp/account/settings.html')

@login_required
def analytics(request):
    return render(request, 'fastbarterApp/account/analytics.html')

@login_required
def deals(request):
    return render(request, 'fastbarterApp/account/deals.html')

@login_required
def favorite(request):
    favorite = Favorite.objects.filter(user=request.user)
    form = ""

    if request.user.is_authenticated:
        favorite = Favorite.objects.filter(user=request.user)
        if request.method == "POST":
            if request.POST["remove_favorite"]:
                Favorite.objects.filter(user=request.user, catalog_id=request.POST["remove_favorite"]).delete()
                form = FavoriteForm()

        else:
            form = FavoriteForm()

    return render(request, 'fastbarterApp/favorite.html', {'favorite': favorite, "form": form})

@login_required
def notifications(request):
    return render(request, 'fastbarterApp/notifications.html')

@login_required
def services(request):
    return render(request, 'fastbarterApp/account/services.html')

@login_required
def chats(request):
    return render(request, 'fastbarterApp/chats.html')

def detail_group(request, group_id):
    detail_group = Groups.objects.get(pk=group_id)
    return render(request, 'fastbarterApp/detail-group.html', {'detail_group': detail_group})

def detail_group_post(request):
    return render(request, 'fastbarterApp/detail-group-post.html')

def new_groups(request):
    groups = Groups.objects.filter()
    return render(request, 'fastbarterApp/new-groups.html', {'groups': groups})
