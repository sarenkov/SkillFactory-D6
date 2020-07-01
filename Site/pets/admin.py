from django.contrib import admin
from .models import Animal, Owner


class Admin(admin.ModelAdmin):
    using = 'postgres'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(Admin, self).get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(Admin, self).formfield_for_foreignkey(db_field, request=request, using=self.using,
                                                           **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(Admin, self).formfield_for_manytomany(db_field, request=request, using=self.using,
                                                           **kwargs)


@admin.register(Animal)
class AnimalAdmin(Admin):
    llist_display = ['name', 'breed', 'type', 'pet_owner']


@admin.register(Owner)
class OwnerAdmin(Admin):
    pass

# admin.site.register(Animal, Admin)
# admin.site.register(Owner, AnimalAdmin)
