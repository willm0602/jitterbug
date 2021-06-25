from django.conf.urls import url 
from .views import AllBunks, UserBunks, bunkView, newBunk

urlpatterns = [
    url(r'^$', AllBunks.as_view(), name = 'bunks'),
    url(r'^(?P<pk>[0-9]+)/$', UserBunks.as_view(), name = 'userbunk'),
    url(r'^bunk/newbunk(?P<sender>[0-9]+)/$',newBunk , name = 'newBunk'),
    url(r'^bunk/(?P<sender>[0-9]+)/$', bunkView, name = 'bunk')
]

