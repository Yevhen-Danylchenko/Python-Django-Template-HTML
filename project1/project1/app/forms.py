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