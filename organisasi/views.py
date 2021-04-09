from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    context= {
        'judul' : 'Organisasi',
        'subjudul' : 'ini adalah halaman untuk organisasi',
    }
        
    
    return render(request, 'organisasi/index.html', context)

def members(request):
    context = {
        'title' : 'Members'
    }
    return render(request, 'organisasi/members.html')

def dokumen(request):
    return render(request, 'organisasi/dokumen.html')