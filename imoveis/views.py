from django.shortcuts import render
from .models import Imovel


# Create your views here.
def index(request):
    imoveis = Imovel.objects.all()
    return render(request, 'index.html',{'imoveis':imoveis})
