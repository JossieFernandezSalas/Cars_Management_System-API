#Author: Jossie Esteban Fernández Salas
# Email: jossie.fernandez.salas@gmail.com
# Linkedin: linkedin.com/in/jossiefernandez

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Car


# Create your views here.
class CarView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            car = Car.objects.filter(id=id).values()
            if car is not None:
                data = {'message': "Success", 'car': list(car)}
            else:
                data = {'message': "Car not found..."}
            return JsonResponse(data)
        else:
            cars = list(Car.objects.values())
            if len(cars) > 0:
                data = {'message': "Success", 'cars': cars}
            else:
                data = {'message': "Car not found..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Car.objects.create(brand=jd['brand'], model=jd['model'], year=jd['year'], color=jd['color'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, id=0):
        jd = json.loads(request.body)
        car = Car.objects.get(id=id)
        if car is not None:
            car.brand = jd['brand']
            car.model = jd['model']
            car.year = jd['year']
            car.color = jd['color']
            car.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Car not found..."}
        return JsonResponse(data)

    def delete(self, request, id=0):
        cars = list(Car.objects.filter(id=id).values())
        if len(cars) > 0:
            Car.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Car not found..."}
        return JsonResponse(data)
