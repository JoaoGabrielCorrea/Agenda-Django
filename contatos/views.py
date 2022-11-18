from django.shortcuts import render
from .models import Contato


# Create your views here.
def index (request):
    contatos =  Contato.objects.all()
    return render (request,'contatos/index.html',{'contatos':contatos})

def index (request):
    return render (request,'contatos/index.html')