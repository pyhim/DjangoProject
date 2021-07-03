from django.shortcuts import render
from django.views.generic import ListView
from .models import Row


# Create your views here.

class RowListView(ListView)