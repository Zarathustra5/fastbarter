"""
URL configuration for fastbarter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('catalog', views.catalog, name="catalog"),
    path('help', views.help, name="help"),
    path('catalog/<int:catalog_id>/', views.detail_catalog, name="detail_catalog"),
    path('new-product', views.new_product, name="new-product"),
    path('reviews', views.reviews, name="reviews"),
    path('account', views.account, name="account"),
    path('edit-profile', views.edit_profile, name="edit-profile"),

    path('settings', views.settings, name="settings"),
    path('analytics', views.analytics, name="analytics"),
    path('deals', views.deals, name="deals"),

    path('favorite', views.favorite, name="favorite"),
    path('services', views.services, name="services"),
    path('chats', views.chats, name="chats"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
