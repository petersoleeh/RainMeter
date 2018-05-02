from django.db import models
from datetime import datetime


import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go


# Create your models here.

class Raindata(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    month = models.CharField(max_length=20)
    rainfall = models.IntegerField(default=0) #rainfall in MM

    def __str__(self):
        return self.month


    @classmethod
    def rain_graph(self):
        data = [
            go.Bar(
                x=[self.month], #Months Jan - Dec
                y=[self.rainfall] # Rainfall in mm
            )
        ]
        plot_url = py.iplot(data, filename='basic-bar')

        return plot_url
