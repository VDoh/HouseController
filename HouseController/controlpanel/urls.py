from django.urls import path,include
from .views import  HomeView, ShowApi, ShowApiDetail #TemperatureMes,

urlpatterns = [
    path('', HomeView.as_view()),
    path('temp/', TemperatureMes.as_view()),
    path('api/', ShowApi.as_view()),
    path('api/<int:pk>', ShowApiDetail.as_view())
]