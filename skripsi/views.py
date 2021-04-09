from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'judul' : 'Scribees',
        'subjudul' : 'your only platform to submit documents',
        'footer' : 'img/BINUS_WEB.png',
    }
    return render(request, 'index.html', context)

#method view
#def about(request):
 #   return render(request, 'about.html')

