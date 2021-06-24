from django.conf.urls import url 
from .views import AllBunks, UserBunks

urlpatterns = [
    url(r'^$', AllBunks.as_view(), name = 'bunks'),
    url(r'^bunk/(?P<pk>[0-9]+)/$', UserBunks.as_view(), name = 'bunk')
]

