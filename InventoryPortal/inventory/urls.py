from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('item/<slug:product_name>/', views.item_detail, name='item_detail'),
]