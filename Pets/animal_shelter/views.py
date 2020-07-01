from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Animal, Owner
from .forms import AnimalForm, OwnerForm


class AnimalView(ListView):
    model = Animal
    template_name = 'animal_shelter/main_page.html'
    context_object_name = 'animals'

    def get_animals(self, animal_type):
        return Animal.objects.filter(type=animal_type).all()


class DogsView(AnimalView):
    def get_queryset(self):
        return super().get_animals('dog')


class CatsView(AnimalView):
    def get_queryset(self):
        return super().get_animals('cat')    


class ParrotsView(AnimalView):
    def get_queryset(self):
        return super().get_animals('parrot')


class AnimalDetail(DetailView):
    model = Animal
    context_object_name = 'animal'
    template_name = 'animal_shelter/main/animal_detail.html'


class OwnerDetail(DetailView):
    model = Owner
    context_object_name = 'owner'
    template_name = 'animal_shelter/main/owner_detail.html'


class AboutUsView(AnimalView):
    template_name = 'animal_shelter/about_us.html'

def render_contacts_page(request):
    template_name = 'animal_shelter/contacts.html'
    return render(request, template_name)

def render_features(request):
    template_name = 'animal_shelter/blank_page.html'
    return render(request, template_name)
