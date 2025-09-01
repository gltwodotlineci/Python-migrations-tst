from django.contrib import admin
from django.urls import path, include
from . import views

handler404 = 'oc_lettings_site.views.views_404'
handler500 = 'oc_lettings_site.views.views_500'

urlpatterns = [
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
