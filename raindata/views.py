from django.shortcuts import render
from .models import Raindata
from .forms import RainForm
from chartit import DataPool, Chart
from django.shortcuts import render_to_response, redirect

# Create your views here.
def index(request):
    data = Raindata.objects.all()


    if request.method == 'POST':
        form = RainForm(request.POST)
        if form.is_valid():
            raindata = form.save(commit=False)
            raindata.save()

            return redirect(index)

    else:

        form = RainForm()

    return render(request,'index.html',{'data':data,'form':form})


def rainfall_graph(request):
    rainfalldata = \
            DataPool(
                series=
                [{'options': {
                    'source': Raindata.objects.all()},
                    'terms': [
                        'month',
                        'rainfall']}
                ])

    cht = Chart(
            datasource = rainfalldata,
            series_options =
                [{'options': {

                    'type': 'line',
                    'stacking': True},

                   'terms':{
                        'month': [
                            'rainfall']

                   }}],

            chart_options =
                {'title':{
                    'text': 'Rainfall Data Year 2018'},

                'xAxis':{
                    'title': {
                        'text': 'Months'}},

                'yAxis':{
                    'title':{
                        'text': 'Rainfall(mm)'}}

                })

    return render(request,'graph.html',{'weatherchart': cht})
