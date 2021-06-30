from django import forms
from .models import Car, CarModel


class CarForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    # vin_number = forms.CharField(max_length=100)

    class Meta:
        model = Car
        fields = "__all__"


class CarModelForm(forms.ModelForm):

    class Meta:
        model = CarModel
        fields = '__all__'
