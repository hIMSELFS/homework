from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(),name='home'),
    path('register/',register, name='register'),
    path('logout/',user_logout, name='logout'),
    path('login/',user_login, name='login'),
    path('test/',TestPage.as_view(),name='test'),
    path('catalog/<str:category_uniCat>/', get_category, name='category'),
]
