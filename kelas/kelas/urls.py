from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from Dashboard.views import about, tambah_barang
from Dashboard.viewset_api import *
from rest_framework import routers

#rest API
router = routers.DefaultRouter()
router.register('jenis', JenisViewset)

def cobax (request):
    return HttpResponse('selamat datang')

def cobay (request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request, 'home.html',konteks)
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', cobay),
    path('about/', about),
    path('addbrg/', tambah_barang),
]
