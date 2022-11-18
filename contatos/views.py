from django.shortcuts import render
import .models import Contatos


# Create your views here.
def index (request):
    contatos =  Contatos.objects.all()
    return render (request,'contatos/index.html'{'contatos:contatos'})

def index (request):
    return render (request,'contatos/index.html')