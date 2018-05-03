from django.db import models
from datetime import datetime
from django.shortcuts import render_to_response


import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go


# Create your models here.

class Raindata(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    month = models.CharField(max_length=20, unique=True)
    rainfall = models.IntegerField(default=0) #rainfall in MM

    def __str__(self):
        return self.month


    @classmethod
    def rain_graph(cls):
        data = [
            go.Bar(
                x=[cls.month], #Months Jan - Dec
                y=[cls.rainfall] # Rainfall in mm
            )
        ]
        plot_url = py.iplot(data, filename='basic-bar')

        return render_to_response('index.html', plot_url)
