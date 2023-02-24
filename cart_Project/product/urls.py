from django.urls import path
from . import views

urlpatterns = [
    path('getproduct/', views.ProductView.as_view(),name="getproduct"),
]