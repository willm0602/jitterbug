from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Bunk, User
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
import json

#view to display all bunks made
class AllBunks(ListView):
    template_name = 'bunks.html'
    context_object_name = 'allbunks'

    def get_queryset(self):
        return Bunk.objects.all().order_by('-sentdate')

#view to display all bunks for a specific user
def userBunksView(request, userID):
    print(userID)
    userBunks = Bunk.objects.filter(Q(sender_id = userID) | Q(receiver_id = userID))
    context = {}
    if len(userBunks):
        context = {
            'bunks': userBunks,
            'userID': userID,
            'name': User.objects.filter(id = userID)[0].username
        }
    else:
        context = {
            'bunks': userBunks,
            'userID': userID,
        }
    return(render(request, "userbunk.html", context))

#view to allow a user to send a bunk to another user
def bunkView(request):
    sender = request.session['id']
    if request.method == "GET":
        context = {
            'sender': sender,
            'username': User.objects.all().filter(pk = sender)[0].username,
            'targets': User.objects.all().filter(
                ~Q(id = sender)
            )
        }
        return(render(request, 'bunk.html', context))
    elif request.method == "POST":
        bunk = Bunk(sender_id = sender, receiver_id = request.POST['target'])
        bunk.save()
        return(HttpResponseRedirect('/'))

#view to handle new users registering
def newUser(request):
    if request.method == "POST":
        context = {'error': "You must enter a profile picture and username"}
        if request.POST['profpic'] and request.POST['username']:
            user = User(username = request.POST['username'], imgurl = request.POST['profpic'])
            user.save()
            request.session['id'] = user.id
            return(HttpResponseRedirect("/"))
        else:
            return(HttpResponseRedirect("/signup"))
    elif request.method == "GET":
        return(render(request, 'signup.html'))

#view to handle users logging in
def login(request):
    users = []
    for u in User.objects.all():
        user = {
            'username': u.username,
            'imgurl': u.imgurl,
            'id': u.id
        }
        users.append(user)
    context = {'users': users}
    if request.method == "POST":
        print(request.POST)
        id = request.POST['userID']
        if len(User.objects.filter(id = id)):
            request.session['id'] = id
            return(HttpResponseRedirect("/"))
        context['error'] = "Invalid user"
    return(render(request, "login.html", context))


class AllUsers(ListView):
    template_name = 'allUsers.html'
    context_object_name = 'users'
    def get_queryset(self):
        return(User.objects.order_by('username'))
