from django.shortcuts import render
from .models import Temperature
from django.views import View
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TemperatureSerializer
import datetime
import RPi.GPIO as GPIO
import time
import w1thermsensor


class HomeView(View):
    template_name = 'main/homepage.html'

    def get(self, request):
        return render(request, self.template_name, {'temp': Temperature.objects.all()})


class TemperatureMes(View):
    template_name = 'main/checktemp.html'

    def get(self, request):

        try:
            sensor = w1thermsensor.W1ThermSensor()
            temperature = sensor.get_temperature()
            date = datetime.datetime.now()

            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(21, GPIO.OUT)
            GPIO.output(21, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(21, GPIO.LOW)
        except:
            print("problem")

        tempo = Temperature.objects.create(temperature=temperature, date=date)

        return render(request, self.template_name, {'temp': tempo})

class ShowApi(APIView):

    def get(self, format=None):

        temperature = Temperature.objects.all()
        serializer = TemperatureSerializer(temperature, many=True)

        return Response(serializer.data)

class ShowApiDetail(APIView):

    def get_object(self, pk):

        try:
            return Temperature.objects.get(pk=pk)
        except Temperature.DoesNotExist:
            raise Http404

    def get(self,request, pk, format=None):

        temperature = self.get_object(pk)
        serializer = TemperatureSerializer(temperature)

        return Response(serializer.data)

