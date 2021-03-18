from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^author/', include('author.urls')),
    url(r'^$',views.index),
    url(r'^crud/',views.crud)

]
