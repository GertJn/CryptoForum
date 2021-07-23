from django.contrib import admin
from django.urls import path
from CryptoForum.views import *
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    path('', home, name='home'),
    path('addInForum/', addInForum, name='addInForum'),
    path('addInComments/', addInComments, name='addInComments'),
]
