from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse
from .models import User, Bunk
from django.urls import reverse


#home page view
def home(req):
    try:
        return render(req, 'home.html', {
            'user': User.objects.get(id=req.session.get('user_id'))
        })
    except:
        return render(req, 'home.html', {
            'user': None
        })

#signup page view
def signup(req):
    return render(req, 'signup.html')

def login(req):
    users = User.objects.all()
    return render(req, "login.html", {"users": users})

#profile page view
def profile(req):
    id = req.session.get('user_id')
    if id is None:
        return HttpResponseRedirect('core:home')
    return render(req, "profile.html", {'user': User.objects.get(id=id)})

#will either show all the bunks for a user id or all bunks
def bunks(req, id=None):
    _bunks = Bunk.objects
    user = None
    if id is None:
        _bunks = _bunks.all()
    else:
        user = User.objects.get(id=id)
        _bunks = _bunks.filter(from_user=user) | _bunks.filter(to_user=user)
    context = {
        "name": "All" if id is None else user.name,
        "bunks": _bunks 
    }
    return render(req, "bunks.html", context=context)

def bunk(req):
    user_id = req.session.get('user_id', None)
    if user_id is None:
        return HttpResponseRedirect(reverse('core:home'))
    user = User.objects.get(id=user_id)
    
    return render(req, 'bunk.html', {
        'user': user,
        'users': User.objects.all().exclude(id=user_id)
    })



#! API Views

def api_signup(req):
    args = req.POST
    name = args.get('name', None)
    img_url = args.get('img_url', None)
    if name is None or img_url is None:
        return HttpResponseBadRequest("Missing name or image")
    new_user = User.objects.create(
        name=name,
        img=img_url
    )
    new_user.save()
    req.session['user_id'] = new_user.id
    return HttpResponseRedirect(reverse('core:home'))

def api_signout(req):
    del req.session['user_id'] 
    return HttpResponseRedirect(reverse('core:home'))

def api_login(req):
    id = req.POST.get('user_id', None)
    if id is not None:
        req.session['user_id'] = id
        return HttpResponseRedirect(reverse('core:home'))
    return HttpResponseBadRequest("Missing ID")

def api_bunk(req):
    data = req.POST
    print('data is', data)
    sender_id = data.get('sender_id', False)
    receiver_id = data.get('receiver_id', False)
    print(sender_id, receiver_id)
    if not (sender_id and receiver_id):
        return HttpResponseBadRequest('One of sender or receiver not provided')

    bunk = Bunk.objects.create(
        from_user=User.objects.get(id=sender_id),
        to_user=User.objects.get(id=receiver_id)
    )
    bunk.save()
    return HttpResponse('Succesfully created new bunk')

