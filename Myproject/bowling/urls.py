from django.urls import path, include
from .views import RowListView
urlpatterns = [
    path("row/", RowListView.as_view(), name="row-list"),
    # path("car/create", CarCreateView.as_view(), name="car-create"),
    # path("car/<int:pk>", CarDetailView.as_view(), name="car-detail"),
]
