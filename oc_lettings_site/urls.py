from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
