from datetime import datetime

from django import forms

class CarSearchForm(forms.Form):
    min_price = forms.IntegerField(
        label = 'Мінімальна ціна',
        required = False,
        min_value = 0,
        widget = forms.NumberInput(attrs={'class': 'form-control'})
    )

    max_price = forms.IntegerField(
        label='Максимальна ціна',
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class CarSearchFormYear(forms.Form):
    min_year = forms.IntegerField(
        label= 'Мінімальний рік',
        required= False,
        min_value= 1900,
        max_value=datetime.now().year,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    max_year = forms.IntegerField(
        label='Максимальний рік',
        required=False,
        min_value=1900,
        max_value=datetime.now().year,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class CarSearchFormModel(forms.Form):
    model = forms.CharField(
        label= 'Модель авто',
        required= False,
        widget= forms.TextInput(attrs={'class': 'form-control'})
    )

class CarSearchFormMark(forms.Form):
    mark = forms.CharField(
        label= 'Марка авто',
        required= False,
        widget= forms.TextInput(attrs={'class': 'form-control'})
    )

class AddCarForm(forms.Form):
    brand = forms.CharField(
        label='Марка',
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    model = forms.CharField(
        label='Модель',
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    year = forms.IntegerField(
        label='Рік',
        required=True,
        min_value=1900,
        max_value=datetime.now().year,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    price = forms.IntegerField(
        label='Ціна',
        required=True,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class DeleteCarForm(forms.Form):
    del_car = forms.IntegerField(
        label='Видалити автомобіль',
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class UpdateCarForm(forms.Form):
    car_id = forms.IntegerField(
        label='Оновити данні автомобіля',
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    brand = forms.CharField(
        label='Марка',
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    model = forms.CharField(
        label='Модель',
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    year = forms.IntegerField(
        label='Рік',
        required=False,
        min_value=1900,
        max_value=datetime.now().year,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    price = forms.IntegerField(
        label='Ціна',
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )


# class AddCarForm(forms.Form):
#     brand = forms.CharField(
#         label= 'Марка',
#         required= True,
#         max_length= 50,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#
#     model = forms.CharField(
#         label='Модель',
#         required=True,
#         max_length=50,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#
#     year = forms.IntegerField(
#         label='Рік',
#         required=True,
#         min_value=1900,
#         max_value=datetime.now().year,
#         widget=forms.NumberInput(attrs={'class': 'form-control'})
#     )
#
#     price = forms.IntegerField(
#         label='Ціна',
#         required=True,
#         min_value=0,
#         widget=forms.NumberInput(attrs={'class': 'form-control'})
#     )





