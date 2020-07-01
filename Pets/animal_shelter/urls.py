from django.urls import path
from . import views

app_name = 'animal_shelter'
urlpatterns = [
    path('', views.AnimalView.as_view(), name='main_page'),
    path('animal/<int:pk>', views.AnimalDetail.as_view(), name='animal'),
    path('owner/<int:pk>', views.OwnerDetail.as_view(), name='owner'),
    path('dogs', views.DogsView.as_view(), name='dogs'),
    path('cats', views.CatsView.as_view(), name='cats'),
    path('parrots', views.ParrotsView.as_view(), name='parrots'),
    path('about', views.AboutUsView.as_view(),  name='about'),
    path('contacts', views.render_contacts_page, name='contacts'),
    path('future_features', views.render_features, name='features')
]
