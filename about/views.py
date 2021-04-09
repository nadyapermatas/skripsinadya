from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    context= {
        
        'heading' : 'About Scribees and SCAC',
        
        
        # 'footer2' : 'about/img/BINUS_WEB.png',
        # 'app_css' : 'about/css/styles.css',
    }
    return render(request, 'about/index.html', context)