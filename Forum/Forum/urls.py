from django.contrib import admin
from django.urls import path
from CryptoForum.views import *
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    url(r"^dashboard/", dashboard, name="dashboard"),
    path('addInForum/', addInForum, name='addInForum'),
    path('addInComments/', addInComments, name='addInComments'),
]
