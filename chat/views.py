from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judulchat' : 'Message Sending'
    }
    return render(request, 'chat/index.html', context)