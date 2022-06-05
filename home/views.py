
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return HttpResponse('<h1>Hello, Nicoleta</h1>')


def show_details_students(request):
    details_students = {
        'all_students': [
            {
                'first_name': 'George',
                'last_name': 'Popescu',
                'age': 30,
                'is_olympic': False
            },
            {
                'first_name': 'Nicoleta',
                'last_name': 'Luchian',
                'age': 36,
                'is_olympic': True
            },
            {
                'first_name': 'Andreea',
                'last_name': 'Ionescu',
                'age': 25,
                'is_olympic': True
            }
        ]
    }

    return render(request, 'home/details_students.html', details_students)


def show_details_cars(request):
    details_cars = {
        'all_cars': [
            {
                'marca': 'BMW',
                'putere': '180 HP',
                'carburant': 'Benzina',
                'hibrid': True
            },
            {
                'marca': 'Volvo',
                'putere': '150 HP',
                'carburant': 'Benzina',
                'hibrid': True
            },
            {
                'marca': 'Mercedes',
                'putere': '200 HP',
                'carburant': 'Motorina',
                'hibrid': False
            }
        ]
    }

    return render(request, 'home/cars_details.html', details_cars)


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'