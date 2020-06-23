from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from p_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('p_library/', include('p_library.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)