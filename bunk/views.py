from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Bunk, User
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

BUNK_COUNT = 5

class AllBunks(ListView):
    template_name = 'bunks.html'
    context_object_name = 'allbunks'

    def get_queryset(self):
        return Bunk.objects.all().order_by('-sentdate')

def userBunksView(request, userID):
    userBunks = Bunk.objects.filter(Q(sender_id = userID) | Q(receiver_id = userID))
    
    context = {
        'bunks': userBunks,
        'userID': userID,
        'name': User.objects.filter(id = userID)[0].username
    }
    return(render(request, "userbunk.html", context))

def bunkView(request, sender):
    context = {
        'sender': sender,
        'targets': User.objects.all().filter(
            ~Q(id = sender)
        )
    }
    return(render(request, 'bunk.html', context))

def newBunk(request, sender):
    bunk = Bunk(sender_id = sender, receiver_id = request.POST['target'])
    bunk.save()
    print("Saved bunk", bunk)
    return(HttpResponseRedirect('/'))
    
def signupForm(request):
    return(render(request, 'signup.html'))

def newUser(request):
    print(request.body)
    return(HttpResponseRedirect('/'))