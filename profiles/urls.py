from django.urls import path
from profiles import views


urlpatterns = [
    path('profiles/', views.indexabc, name='profiles_index'),
    # path('profiles/<str:username>/', views.profile, name='profile'),
]
