from django.urls import path
from . import views

app_name = 'pets'
urlpatterns = [
    path('', views.AnimalView.as_view(), name='main_page'),
]
