from django.urls import path,include
from .views import  HomeView, TemperatureMes

urlpatterns = [
    path('', HomeView.as_view()),
    path('temp/', TemperatureMes.as_view())
]