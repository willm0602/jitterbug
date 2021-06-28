from django.conf.urls import url 
from .views import AllBunks, bunkView, newBunk, signupForm, userBunksView, newUser, login, allUsers

app_name = 'bunk'

urlpatterns = [
    #/ index view, shows all bunks
    url(r'^$', AllBunks.as_view(), name = 'bunks'),

    #/{id}, shows all bunks involving a user with a specified id
    url(r'^(?P<userID>[0-9]+)/$', userBunksView, name = 'userbunk'),

    #bunk/newbunk{sender}, makes a new bunk from sender to a recipient that is received from the post request
    url(r'^bunk/newbunk(?P<sender>[0-9]+)/$',newBunk , name = 'newBunk'),

    #bunk/, allows the user to chose someone to bunk TODO: merge with newBunk
    url(r'^bunk/$', bunkView, name = 'bunk'),

    #/signup, allows the users to register TODO: Merge with newuser
    url(r'^signup/$', signupForm, name = 'signupForm'),

    #/newuser handles POST requests from registration from signupForm
    url(r'^newuser/$', newUser, name = 'newuser'),

    #/login logs in a user
    url(r'^login/', login, name = 'login'),

    #/users gets all users
    url(r'^users/$', allUsers, name = 'allUsers')
]
