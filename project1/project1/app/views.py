from django.http import HttpResponse
from django.shortcuts import render

from project1.app.forms import CarSearchForm, CarSearchFormYear, CarSearchFormModel, CarSearchFormMark


def show_car_by_id(request, car_id):

    context = {
        'car_id': car_id,
        'car': cars[car_id]
    }

    return render(request, 'app/show_car_by_id.html', context)


cars = {
    1: {
        "Марка": "VW",
        "Модель": "Passat b5",
        "Рік": 2007,
        "Ціна": 5000
    },
    2: {
        "Марка": "VW",
        "Модель": "Golf 5",
        "Рік": 2012,
        "Ціна": 7000
    },
    3: {
        "Марка": "Audi",
        "Модель": "A4",
        "Рік": 2012,
        "Ціна": 12000
    }
}

def search_cars(request):
    filtered_cars = []

    form = CarSearchForm(request.GET or None)
    form_year = CarSearchFormYear(request.GET or None)
    form_model = CarSearchFormModel(request.GET or None)
    form_mark = CarSearchFormMark(request.GET or None)
    if form.is_valid() and form_year.is_valid() and form_model.is_valid() and form_mark.is_valid():
        min_price = form.cleaned_data.get('min_price', 0) or 0
        max_price = form.cleaned_data.get('max_price') or float('inf')
        min_year = form_year.cleaned_data.get('min_year', 0) or 0
        max_year = form_year.cleaned_data.get('max_year') or float('inf')
        model_car = form_model.cleaned_data.get('model', '').lower()
        mark_car = form_mark.cleaned_data.get('mark', '').lower()

        for car_id, car in cars.items():
            if (min_price <= car["Ціна"] <= max_price and min_year <= car["Рік"] <= max_year
                and model_car in car["Модель"].lower() and mark_car in car["Марка"].lower()):
                filtered_cars.append(car)

    context = {
        'filtered_cars': filtered_cars,
        'form': form,
        'form_year': form_year,
        'form_model': form_model,
        'form_mark': form_mark
    }
    return render(request, 'app/search_cars.html', context)

def hello_world(request):
    return render(request, 'app/index.html')


def show_info(request):

    context = {
        'cars':cars
    }

    return render(request, 'app/car_list.html', context)

def show_details(request):
    context = {
        'cars':cars
    }
    return render(request, 'app/car_details.html', context)

def say_hello(request, name):
    return HttpResponse(f"Hello, {name}")


def greeting(request):
    return HttpResponse("Вітаємо на нашому сайті!")