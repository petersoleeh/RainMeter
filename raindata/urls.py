from django.urls import path
from . import views

urlpatterns=[
    # the landing page
    path('',views.index,name='index'),

    #graph page
    path('rainfall_graph/', views.rainfall_graph,name='rainfall_graph')

]
