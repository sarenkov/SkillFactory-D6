from django.forms import ModelForm

from .models import Animal, Owner


class AnimalForm(ModelForm):

    class Meta:
        fields = '__all__'
        model = Animal


class OwnerForm(ModelForm):

    class Meta:
        model = Owner
        fields = '__all__'
