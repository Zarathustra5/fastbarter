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
    formChat = NewChatForm(initial={'user1': request.user.id, 'user2': detail_catalog.user.id, 'catalog': catalog_id})

    if request.user.is_authenticated & (request.method == "POST"):
        favorite = Favorite.objects.filter(user=request.user)
        if request.POST["remove_favorite"]:
            Favorite.objects.filter(user=request.user, catalog_id=catalog_id).delete()
        else:
            Favorite.objects.create(user=request.user, catalog_id=catalog_id)

    return render(request, 'fastbarterApp/detail-catalog.html', {'detail_catalog': detail_catalog, "favorite": favorite, "form_chat": formChat })

def catalog(request):
    # return HttpResponse('<h4>About</h4>')
    search = request.GET.get("s")
    catalog = Catalog.objects.filter(is_published=True)
    favorite = ""
    form = ""
    filterForm = FilterForm()

    if (request.method == "POST") & (not request.user.is_authenticated):
        return redirect('/account/login')

    if request.user.is_authenticated:
        favorite = Favorite.objects.filter(user=request.user)
        if request.method == "POST":
            if request.POST["filter"]:
                catalog = Catalog.objects.filter(is_published=True, price__gte=request.POST["price_from"], price__lte=request.POST["price_to"])
            elif request.POST["remove_favorite"]:
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

    return render(request, 'fastbarterApp/catalog.html', {'catalog': catalog, 'search': search, "form": form, "favorite": favorite, "filter_form": filterForm})

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
    chats1 = Chats.objects.filter(user1=request.user)
    chats2 = Chats.objects.filter(user2=request.user)
    chatsLength = len(chats1) + len(chats2)
    if chatsLength == 0:
        currentChat = {}
    elif len(chats1) == 0:
        currentChat = chats2[0]
    else:
        currentChat = chats1[0]
    if request.method == "POST":
        if request.POST["message_form"]:
            form = NewMessageForm(request.POST)
            form.save()
        elif request.POST["switch_chat"]:
            currentChat = Chats.objects.get(pk=request.POST["switch_chat"])
        else:
            form = NewChatForm(request.POST)
            form.save()
            #Chats.objects.create(user1=request.user, user2=request.POST["user"], catalog_id=request.POST["catalog"])
    if currentChat:
        messages = Messages.objects.filter(chat=currentChat)
    else:
        messages = []
    formMessage = NewMessageForm(initial={'user': request.user, 'chat': currentChat })
    return render(request, 'fastbarterApp/chats.html', {'chats1': chats1, 'chats2': chats2, 'chats_length': chatsLength, 'messages': messages, 'current_chat': currentChat, 'form_message': formMessage})

def detail_group(request, group_id):
    detail_group = Groups.objects.get(pk=group_id)
    return render(request, 'fastbarterApp/detail-group.html', {'detail_group': detail_group})

def detail_group_post(request):
    return render(request, 'fastbarterApp/detail-group-post.html')

def new_groups(request):
    groups = Groups.objects.filter()
    return render(request, 'fastbarterApp/new-groups.html', {'groups': groups})
