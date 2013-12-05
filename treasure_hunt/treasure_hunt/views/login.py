# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_POST, require_GET
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

@require_GET
@login_required
def user_logout(request):
  from django.contrib.auth import logout
  logout(request)
  c = {}
  c.update(csrf(request))
  return render_to_response("index.html", c)

@require_POST
def login(request):
  from django.contrib.auth import authenticate, login
  from treasure_hunt.models import ObjectTip

  data = {}

  user = authenticate(username=request.POST['name'], password=request.POST['password'])
  if user is not None:
    login(request=request, user=user)
  else:
    user = create_new_user(username=request.POST['name'], password=request.POST['password'])

  data['username'] = user.username

  data['tips'] = []

  for tip in ObjectTip.objects.all():
    data['tips'].append({'name': u"Dica {0}".format(tip.id), 'id': tip.id})


  return render_to_response("home.html", data)

@require_GET
def home(request):
  c = {}
  c.update(csrf(request))
  return render_to_response("index.html", c)

def create_new_user(username, password):
  from django.contrib.auth.models import User
  user = User(username=username)
  # the leap of the cat
  user.set_password(password)
  user.save()

  return user
