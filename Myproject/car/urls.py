from django.urls import path, include
from .views import (
    CarListView, CarDetailView, CarCreateView,
    CarModelListView, CarModelDetailView, CarModelCreateView
)
urlpatterns = [
    path("car/", CarListView.as_view(), name="car-list"),
    path("car/create", CarCreateView.as_view(), name="car-create"),
    path("car/<int:pk>", CarDetailView.as_view(), name="car-detail"),
    path('car_model/', CarModelListView.as_view(), name='car-model-list'),
    path('car_model/create', CarModelCreateView.as_view(), name='car-model-create'),
    path('car_model/<int:pk>', CarModelDetailView.as_view(), name='car-model-detail')
]
