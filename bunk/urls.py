from django.conf.urls import url 
from .views import AllBunks

urlpatterns = [
    url(r'^$', AllBunks.as_view(), name = 'bunks')
]

