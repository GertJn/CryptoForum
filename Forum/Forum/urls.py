from django.contrib import admin
from django.urls import path
from CryptoForum.Forum.CryptoForum.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addInForum/', addInForum, name='addInForum'),
    path('addInComments/', addInComments, name='addInComments'),
]
