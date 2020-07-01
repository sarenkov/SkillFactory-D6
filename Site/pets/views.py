from django.shortcuts import render
from django.views.generic import ListView
from .models import Animal
from .forms import AnimalForm

# Create your views here.
class AnimalView(ListView):
    model = Animal
    form_class = AnimalForm
    template_name = 'pets/main_page.html'