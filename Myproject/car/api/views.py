from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from Myproject.car.models import Company
from .serializer import CompanySerializer


class CompanyViewSet(ModelViewSet):
    pass

