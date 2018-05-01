from django.shortcuts import render
from .models import Raindata

# Create your views here.
def index(request):
    data = Raindata.objects.all()

    return render(request,'index.html',{'data':data})
