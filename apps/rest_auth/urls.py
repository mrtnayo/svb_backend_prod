from django.urls import path

from apps.rest_auth.views import login, logout, registration


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', registration, name='registration'),
    path('logout/', logout, name='logout')
]
