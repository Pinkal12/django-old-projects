from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.home,name='home'), #url for form page 
    path('datatable/',views.datatable,name='datatable'), #url for datatable page 
]
