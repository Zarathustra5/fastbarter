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
from .functions import *

def index(request):
    return render(request, 'fastbarterApp/index.html')

def detail_catalog(request, catalog_id):
    detail_catalog = Catalog.objects.get(pk=catalog_id)
    favorite = ""
    if request.user.is_authenticated:
        formDeal = NewDealForm(initial={'user_owner': request.user.id, 'user_customer': detail_catalog.user.id, 'owner_product': catalog_id})
        if detail_catalog.category_exchange:
            userCatalog = Catalog.objects.filter(user=request.user, category=detail_catalog.category_exchange)
        else:
            userCatalog = Catalog.objects.filter(user=request.user)
    else:
        formDeal = NewDealForm()
        userCatalog = {}
    reviews = Reviews.objects.filter(userTo=detail_catalog.user.id)

    if request.user.is_authenticated & (request.method == "POST"):
        favorite = Favorite.objects.filter(user=request.user)
        if request.POST["remove_favorite"]:
            Favorite.objects.filter(user=request.user, catalog_id=catalog_id).delete()
        else:
            Favorite.objects.create(user=request.user, catalog_id=catalog_id)

    return render(request, 'fastbarterApp/detail-catalog.html', {'detail_catalog': detail_catalog, "favorite": favorite, "form_deal": formDeal, "reviews": reviews, "userCatalog": userCatalog })

def catalog(request):
    # return HttpResponse('<h4>About</h4>')
    search = request.GET.get("s")
    catalog = Catalog.objects.filter(is_published=True)
    favorite = ""
    form = ""
    filterForm = FilterForm()
    categories = Category.objects.filter()

    if (request.method == "POST") & (not request.user.is_authenticated):
        return redirect('/account/login')

    if request.user.is_authenticated:
        favorite = Favorite.objects.filter(user=request.user)
        if request.method == "POST":
            if request.POST["filter"]:
                arr_category = request.POST.getlist("category")
                price_from = request.POST.get("price_from")
                price_to = request.POST.get("price_to")
                if not(price_from):
                    price_from = 0
                if not(price_to):
                    price_to = 99999999999
                if arr_category:
                    catalog = Catalog.objects.filter(is_published=True, price__range=(price_from, price_to), category__in=arr_category)
                else:
                    catalog = Catalog.objects.filter(is_published=True, price__range=(price_from, price_to))
            elif request.POST.get("remove_favorite"):
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

    return render(request, 'fastbarterApp/catalog.html', {'catalog': catalog, 'search': search, "form": form, "favorite": favorite, "filter_form": filterForm, "categories": categories})

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

    createMediaFileHTML(reviews)

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
    currentDeals1 = Deals.objects.filter(user_owner=request.user, status=False)
    currentDeals2 = Deals.objects.filter(user_customer=request.user, status=False)
    finishedDeals1 = Deals.objects.filter(user_owner=request.user, status=True)
    finishedDeals2 = Deals.objects.filter(user_customer=request.user, status=True)
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
    # Личные чаты
    currentChat = ""
    currentGroupChat = ""
    if request.method == "POST":
        if request.POST["query_type"] == "create_new_chat":
            try:
                Deals.objects.get(user_owner=request.POST["user_owner"], user_customer=request.POST["user_customer"], owner_product=request.POST["owner_product"], customer_product=request.POST["customer_product"])
            except Deals.DoesNotExist:
                formDeal = NewDealForm(request.POST)
                createdDeal = formDeal.save()
                formChat = NewChatForm()
                obj = formChat.save(commit=False)
                obj.deal = createdDeal
                currentChat = obj.save()
        elif request.POST["query_type"] == "switch_chat":
            currentChat = Chats.objects.get(pk=request.POST["switch_chat"])
        elif request.POST["query_type"] == "switch_group_chat":
            currentGroupChat = Groups.objects.get(pk=request.POST["switch_group_chat"])
        elif request.POST["query_type"] == "message_form":
            currentChat = Chats.objects.get(pk=request.POST["chat"])
            form = NewMessageForm(request.POST, request.FILES)
            form.save()
        elif request.POST["query_type"] == "group_message_form":
            currentGroupChat = Groups.objects.get(pk=request.POST["group"])
            form = NewGroupMessageForm(request.POST, request.FILES)
            form.save()
        elif request.POST["query_type"] == "delete_chat":
            Chats.objects.filter(pk=request.POST["delete_chat"]).update(is_deleted_user_owner=True)
    owner_deals = Deals.objects.filter(user_owner=request.user)
    owner_chats = []
    for deal in owner_deals:
        try:
            chats = Chats.objects.get(deal=deal, is_deleted_user_owner=False)
        except Chats.DoesNotExist:
            chats = None
        if chats:
            owner_chats.append(chats)
    customer_deals = Deals.objects.filter(user_customer=request.user)
    customer_chats = []
    for deal in customer_deals:
        try:
            chats = Chats.objects.get(deal=deal, is_deleted_user_customer=False)
        except Chats.DoesNotExist:
            chats = None
        if chats:
            customer_chats.append(chats)
    chatsLength = len(owner_chats) + len(customer_chats)
    formGroupMessage = NewGroupMessageForm()
    if currentGroupChat:
        messages = GroupMessages.objects.filter(group=currentGroupChat)
        formGroupMessage = NewGroupMessageForm(initial={'user': request.user, 'group': currentGroupChat.id })
    elif currentChat:
        messages = Messages.objects.filter(chat=currentChat)
    else:
        messages = []
    formMessage = NewMessageForm(initial={'user': request.user, 'chat': currentChat })
    createMediaFileHTML(messages)
    if not currentChat and not currentGroupChat:
        if chatsLength == 0:
            currentChat = {}
        elif len(owner_chats) == 0:
            currentChat = customer_chats[0]
        else:
            currentChat = owner_chats[0]

    # Беседы сообществ
    user_groups= []
    subscribtions = Participants.objects.filter(user=request.user)
    for subscribtion in subscribtions:
        try:
            group = Groups.objects.get(pk=subscribtion.group.id)
        except Groups.DoesNotExist:
            group = None
        if chats:
            user_groups.append(group)
    groups_length = len(user_groups)

    return render(request, 'fastbarterApp/chats.html', {'owner_chats': owner_chats, 'customer_chats': customer_chats, 'chats_length': chatsLength, 'messages': messages, 'current_chat': currentChat, 'form_message': formMessage, 'user_groups': user_groups, 'groups_length': groups_length, 'current_group_chat': currentGroupChat, 'form_group_message': formGroupMessage})

def detail_group(request, group_id):
    detail_group = Groups.objects.get(pk=group_id)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('/account/login')
        elif request.POST["query_type"] == "join_group":
            Participants.objects.create(user=request.user, group_id=group_id)
        elif request.POST["query_type"] == "leave_group":
            Participants.objects.filter(user=request.user, group_id=group_id).delete()
        return HttpResponseRedirect('./')
    participants = Participants.objects.filter(group=group_id)
    participants_count = len(participants) + 1
    is_user_participant = False
    if request.user.id == detail_group.user.id:
        is_user_admin = True
    else:
        is_user_admin = False
        for participant in participants:
            if request.user.id == participant.user.id:
                is_user_participant = True
                break
    posts = Posts.objects.filter(group=group_id)
    createMediaFileHTML(posts)
    return render(request, 'fastbarterApp/detail-group.html', {'detail_group': detail_group,'participants': participants[:7],'participants_count': participants_count,'is_user_participant': is_user_participant,'is_user_admin': is_user_admin, 'posts': posts})

def detail_group_post(request):
    return render(request, 'fastbarterApp/detail-group-post.html')

def groups(request):
    groups = Groups.objects.filter()
    participants = {}
    if request.user.id:
        participants = Participants.objects.filter(user=request.user)
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

@login_required
def new_post(request):
    success = False
    group_id = ""
    if request.method == "POST":
        if request.POST.get("group_id"):
            group_id = request.POST.get("group_id")
            form = NewPostForm()
        else:
            form = NewPostForm(request.POST, request.FILES)
            obj = form.save(commit=False)
            obj.save()
            #form.save()
            success = True
    else:
        form = ""
    return render(request, 'fastbarterApp/new-post.html', {"form": form, "success": success, "group_id": group_id})

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
