from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('senac_projeto.urls')),  # Incluindo as URLs do aplicativo 'senac_projeto'
]

