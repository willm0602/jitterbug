from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup),
    path('login', views.login),
    path('profile', views.profile),
    path('bunks', views.bunks),
    path('bunks/<int:id>', views.bunks),
    path('bunk', views.bunk),

    path('api/signup', views.api_signup),
    path('api/signout', views.api_signout),
    path('api/login', views.api_login),
    path('api/bunk', views.api_bunk)
]
