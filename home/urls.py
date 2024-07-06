#changes
from django.contrib import admin
from django.urls import path, include
from home import views
from django.urls import path
from . import views
from .views import order_view

urlpatterns = [
    path('order/', order_view, name='order_view'),
    path('',views.index, name='index'),

    path("", views.index, name='home'),
     path("order", views.order, name='order.html'),
    path("contact", views.contact, name='contact.html'),
    path("login", views.login, name='login.html'),
     path("designer-detail", views.designer_detail, name='designer-detail.html'), # type: ignore
    path("design-list", views.design_list, name='design-list.html'),
    path("my-account", views.myaccount, name='my-account.html'),
]
