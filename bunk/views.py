from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Bunk, User

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
        allBunks = Bunk.objects.get(pk = id)
        print(allBunks)
        return Bunk.objects.filter(Q(sender_id=id) | Q(receiver_id=id)).order_by('-sentdate')
        

