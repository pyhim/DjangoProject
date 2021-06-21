from django.db import models
from django.urls import reverse


# Create your models here.
class Car(models.Model):
    types_short = [
        'ЛГ',
        'ВЖ',
        'ГР'
    ]
    types = [
        (types_short[0], 'Легковая'),
        (types_short[1], 'Внедорожник'),
        (types_short[2], 'Грузовик')
    ]
    name = models.CharField(max_length=100)
    vin_number = models.CharField(max_length=100)
    color = models.CharField(max_length=100, default='White')
    made_date = models.DateField(default='yyyy-mm-dd')
    type_of_car = models.CharField(
        choices=types,
        default=types[0],
        max_length=2
    )
    car_model = models.ForeignKey(
        "car.CarModel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="cars"
    )

    def company(self):
        if self.car_model:
            return self.car_model.company
        return None

    def __str__(self):
        return f"Name:{self.name} vin_number: {self.vin_number}"

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ["car_model"]


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey("car.Company", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"
