from django.db import models
from django.urls import reverse_lazy


class Animal(models.Model):

    animal_types = [
        ('cat', 'Кошка'),
        ('dog', 'Собака'),
        ('parrot', 'Папугай')
    ]

    name = models.fields.CharField(max_length=100)
    breed = models.fields.TextField()
    description = models.fields.TextField()
    receipt_date = models.fields.DateTimeField(auto_now_add=True)
    type = models.fields.TextField(choices=animal_types)
    avatar = models.ImageField(null=True, blank=True)
    pet_owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('pets:main_page')

    def __str__(self):
        return f"{self.type} {self.name}"

    class Meta:
        ordering = ['type']
        db_table = 'Animals'
        verbose_name = 'Animal'
        verbose_name_plural = 'Animals'


class Owner(models.Model):
    name = models.fields.CharField(max_length=50)
    surname = models.fields.CharField(max_length=50, null=True)
    mobile = models.fields.CharField(max_length=12, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('pets:main_page')

    def __str__(self):
        return f"{self.name} {self.surname or self.mobile or self.address or self.email or ''}"

    class Meta:
        ordering = ['name']
        db_table = 'Owners'
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'