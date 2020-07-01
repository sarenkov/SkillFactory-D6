from django.contrib import admin
from .views import Animal, Owner
from .forms import AnimalForm, OwnerForm


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    form = AnimalForm
    list_display = ['name', 'breed', 'description', 'pet_owner']
    list_filter = ['type']
    actions = ['duplicate',]

    def duplicate(self, request, queryset):
        for obj in queryset:
            obj.id = None
            obj.save()

    duplicate.short_description = "Копировать выбранные записи"


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    form = OwnerForm
    list_display = ['name', 'surname', 'mobile']
