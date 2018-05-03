from django.shortcuts import render
from .models import Raindata
from .forms import RainForm

# Create your views here.
def index(request):
    data = Raindata.objects.all()
    # graph = Raindata.rain_graph()

    if request.method == 'POST':
        form = RainForm(request.POST)
        if form.is_valid():
            raindata = form.save(commit=False)
            raindata.save()
            form = RainForm()

    else:

        form = RainForm()

    return render(request,'index.html',{'data':data,'form':form})
