from django.conf.urls import url 
from .views import AllBunks, bunkView, userBunksView, newUser, login, allUsers

app_name = 'bunk'

urlpatterns = [
    #/ index view, shows all bunks
    url(r'^$', AllBunks.as_view(), name = 'bunks'),

    #/{id}, shows all bunks involving a user with a specified id
    url(r'^(?P<userID>[0-9]+)/$', userBunksView, name = 'userbunk'),

    #bunk/, allows the user to chose someone to bunk 
    url(r'^bunk/$', bunkView, name = 'bunk'),

    #/signup, allows the users to register 
    url(r'^register/$', newUser, name = 'newuser'),

    #/login logs in a user
    url(r'^login/', login, name = 'login'),

    #/users gets all users
    url(r'^users/$', allUsers, name = 'allUsers')
]
