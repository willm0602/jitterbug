from django.conf.urls import url 
from .views import AllBunks, bunkView, newBunk, signupForm, userBunksView

urlpatterns = [
    url(r'^$', AllBunks.as_view(), name = 'bunks'),
    url(r'^(?P<userID>[0-9]+)/$', userBunksView, name = 'userbunk'),
    url(r'^bunk/newbunk(?P<sender>[0-9]+)/$',newBunk , name = 'newBunk'),
    url(r'^bunk/(?P<sender>[0-9]+)/$', bunkView, name = 'bunk'),
    url(r'^signup/$', signupForm, name = 'signupForm'),
    url(r'^newuser/$', signupForm, name = 'signupForm')
]

