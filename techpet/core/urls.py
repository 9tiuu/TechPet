from django.urls import path
from . import views
from .views import PetsDetail

urlpatterns = [
    path('', views.Home, name='home'),
    path('pet/<uuid:pk>/', PetsDetail.as_view(), name='pet'),
]