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
        return Bunk.objects.all()

class UserBunks(ListView):
    template_name = "userbunk.html"
    context_object_name = "bunks"
    
    def get_queryset(self):
        id = self.kwargs['pk']
        allBunks = Bunk.objects.all()
        print(allBunks)
        return Bunk.objects.filter(Q(sender_id=id) | Q(receiver_id=id)).order_by('-sentdate')


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
    

