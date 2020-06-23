from django.contrib import admin
from .models import Book, Author, Friend, Publisher

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Friend)
admin.site.register(Publisher)
