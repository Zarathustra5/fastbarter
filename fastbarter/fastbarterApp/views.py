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
from django.http import JsonResponse
import json
#from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CatalogSerializer
from django.forms import model_to_dict


def index(request):
    return render(request, 'fastbarterApp/index.html')

def detail_catalog(request, catalog_id):
    detail_catalog = Catalog.objects.get(pk=catalog_id)
    favorite = ""
    if request.user.is_authenticated:
        formChat = NewChatForm(initial={'user1': request.user.id, 'user2': detail_catalog.user.id, 'catalog': catalog_id})
        if detail_catalog.category_exchange:
            userCatalog = Catalog.objects.filter(user=request.user, category=detail_catalog.category_exchange)
        else:
            userCatalog = Catalog.objects.filter(user=request.user)
    else:
        formChat = NewChatForm()
        userCatalog = {}
    reviews = Reviews.objects.filter(userTo=detail_catalog.user.id)

    if request.user.is_authenticated & (request.method == "POST"):
        favorite = Favorite.objects.filter(user=request.user)
        if request.POST["remove_favorite"]:
            Favorite.objects.filter(user=request.user, catalog_id=catalog_id).delete()
        else:
            Favorite.objects.create(user=request.user, catalog_id=catalog_id)

    return render(request, 'fastbarterApp/detail-catalog.html', {'detail_catalog': detail_catalog, "favorite": favorite, "form_chat": formChat, "reviews": reviews, "userCatalog": userCatalog })

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

@login_required
def reviews(request):
    success = False
    detail_catalog = ''
    userTo = ''
    reviews = ''
    rating = ["1", "2", "3", "4", "5"]
    if request.method == "POST":
        if request.POST["submit-new-review"]:
            form = NewReviewForm(request.POST, request.FILES)
            form.save()
            success = True
        detail_catalog = Catalog.objects.get(pk=request.POST["catalog"])
        userTo = detail_catalog.user
        reviews = Reviews.objects.filter(userTo=userTo)
        form = NewReviewForm(initial={'user': request.user, 'userTo': userTo, 'catalog': request.POST["catalog"] })

    else:
        return redirect('/catalog')

    return render(request, 'fastbarterApp/reviews.html', {"form": form, "success": success, "userTo": userTo, "detail_catalog": detail_catalog, "reviews": reviews, "rating": rating})

@login_required
def my_reviews(request):
    rating = ["1", "2", "3", "4", "5"]
    reviews = Reviews.objects.filter(userTo=request.user)
    return render(request, 'fastbarterApp/account/my-reviews.html', {"reviews": reviews, "rating": rating})

@login_required
def account(request):
    reviews = Reviews.objects.filter(userTo=request.user)
    catalog = Catalog.objects.filter(user=request.user)
    return render(request, 'fastbarterApp/account/index.html', {'catalog': catalog, "reviews": reviews})

@login_required
def edit_profile(request):
    reviews = Reviews.objects.filter(userTo=request.user)
    if request.method == "POST":
        #form = EditProfileForm(request.POST)
        #CustomUsers.objects.filter(pk=request.user.id).update(name=request.POST["name"], phone_number=request.POST["phone_number"])
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        form.save()

    else:
        form = EditProfileForm(initial={'name': request.user.name, 'phone_number': request.user.phone_number, 'email': request.user.email, 'city': request.user.city })

    return render(request, "fastbarterApp/account/edit-profile.html", {"form": form, "reviews": reviews})

@login_required
def settings(request):
    reviews = Reviews.objects.filter(userTo=request.user)
    return render(request, 'fastbarterApp/account/settings.html', {"reviews": reviews})

@login_required
def analytics(request):
    reviews = Reviews.objects.filter(userTo=request.user)
    return render(request, 'fastbarterApp/account/analytics.html', {"reviews": reviews})

@login_required
def deals(request):
    if request.method == "POST":
        if request.POST["submit-finish-deal"]:
            deal = Deals.objects.get(pk=request.POST["deal"])
            deal.status = True
            deal.save()
    currentDeals1 = Deals.objects.filter(user1=request.user, status=False)
    currentDeals2 = Deals.objects.filter(user2=request.user, status=False)
    finishedDeals1 = Deals.objects.filter(user1=request.user, status=True)
    finishedDeals2 = Deals.objects.filter(user2=request.user, status=True)
    reviews = Reviews.objects.filter(userTo=request.user)
    return render(request, 'fastbarterApp/account/deals.html', {"reviews": reviews,"currentDeals1": currentDeals1,"currentDeals2": currentDeals2,"finishedDeals1": finishedDeals1,"finishedDeals2": finishedDeals2 })

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
    reviews = Reviews.objects.filter(userTo=request.user)
    return render(request, 'fastbarterApp/account/services.html', {"reviews": reviews})

@login_required
def chats(request):
    currentChat = ""
    if request.method == "POST":
        if request.POST["create_new_chat"]:
            form = NewChatForm(request.POST)
            formDeal = NewDealForm(request.POST)
            form.save()
            formDeal.save()
            currentChat = Chats.objects.filter(user1=request.user).last()
    chats1 = Chats.objects.filter(user1=request.user)
    chats2 = Chats.objects.filter(user2=request.user)
    chatsLength = len(chats1) + len(chats2)
    if request.method == "POST":
        if request.POST["message_form"]:
            currentChat = Chats.objects.get(pk=request.POST["chat"])
            form = NewMessageForm(request.POST)
            form.save()
        elif request.POST["switch_chat"]:
            currentChat = Chats.objects.get(pk=request.POST["switch_chat"])
    if currentChat:
        messages = Messages.objects.filter(chat=currentChat)
    else:
        messages = []
    formMessage = NewMessageForm(initial={'user': request.user, 'chat': currentChat })
    if not currentChat:
        if chatsLength == 0:
            currentChat = {}
        elif len(chats1) == 0:
            currentChat = chats2[0]
        else:
            currentChat = chats1[0]
    return render(request, 'fastbarterApp/chats.html', {'chats1': chats1, 'chats2': chats2, 'chats_length': chatsLength, 'messages': messages, 'current_chat': currentChat, 'form_message': formMessage})

def detail_group(request, group_id):
    detail_group = Groups.objects.get(pk=group_id)
    return render(request, 'fastbarterApp/detail-group.html', {'detail_group': detail_group})

def detail_group_post(request):
    return render(request, 'fastbarterApp/detail-group-post.html')

def groups(request):
    groups = Groups.objects.filter()
    participants = {}
    if request.user.id:
        participants = Participants.objects.filter(user=request.user)
    if request.method == "POST":
        if request.POST["join_group"]:
            Participants.objects.create(user=request.user, group_id=request.POST["join_group"])
    return render(request, 'fastbarterApp/groups.html', {'groups': groups,'participants': participants})

@login_required
def new_group(request):
    success = False
    if request.method == "POST":
        form = NewGroupForm(request.POST, request.FILES)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        #form.save()
        success = True

    else:
        form = NewGroupForm()

    return render(request, 'fastbarterApp/new-group.html', {"form": form, "success": success})

def check_reviews(request):
    success = False
    detail_catalog = ''
    userTo = ''
    reviews = ''
    rating = ["1", "2", "3", "4", "5"]
    if request.method == "POST":
        detail_catalog = Catalog.objects.get(pk=request.POST["catalog"])
        userTo = detail_catalog.user
        reviews = Reviews.objects.filter(userTo=userTo)

    else:
        return redirect('/catalog')

    return render(request, 'fastbarterApp/check-reviews.html', {"success": success, "userTo": userTo, "detail_catalog": detail_catalog, "reviews": reviews, "rating": rating})

def update_chat(request):
    #messages = Messages.objects.filter(chat=currentChat)
    #results = [ob.as_json() for message in Messages.objects.all()]
    results = [ json.dumps({'id': message.id, 'created_at': str(message.created_at), 'text': message.text, 'chat': str(message.chat.id), 'user': str(message.user.id)}) for message in Messages.objects.all()]
    return JsonResponse({'latest_results_list':results})

class CatalogAPIView(APIView):
    def get(self, request):
        queryset = Catalog.objects.all()
        return Response({'posts': CatalogSerializer(queryset, many=True).data})

    def post(self, request):
        serializer = CatalogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category = Category.objects.get(pk=request.data['category_id'])
        post_new = Catalog.objects.create(
            title=request.data['title'],
            short_desc=request.data['short_desc'],
            category=category,
        )
        return Response({'new_post': CatalogSerializer(post_new).data})