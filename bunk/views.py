from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Bunk, User

BUNK_COUNT = 5

class AllBunks(ListView):
    template_name = 'bunks.html'
    context_object_name = 'allbunks'

    def get_queryset(self):
        return Bunk.objects.all()
