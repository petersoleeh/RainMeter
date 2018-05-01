from django.urls import path
from . import views


urlpatterns=[
    # the landing page
    path('',views.index,name='index'),

]
