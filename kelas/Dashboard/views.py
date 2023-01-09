from django.shortcuts import render
from Dashboard.forms import FormBarang

# Create your views here.


def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form':form,
    }
    return render(request, 'tambah_barang.html',konteks)

def about(request):
    titelnya="about"
    konteks = {
        'titel':titelnya,
    }
    return render (request,'about.html',konteks)