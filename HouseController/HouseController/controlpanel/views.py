from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Temperature
from django.views import View
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
