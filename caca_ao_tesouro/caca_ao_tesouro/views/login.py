# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_POST, require_GET
from django.core.context_processors import csrf

@require_POST
def login(request):
  from django.contrib.auth import authenticate, login

  print request.POST['name'], request.POST['password']
  user = authenticate(username=request.POST['name'], password=request.POST['password'])
  if user is not None:
    login(request=request, user=user)
    message = u'Logado!'
  else:
    create_new_user(username=request.POST['name'], password=request.POST['password'])
    message = u'Criado novo usuário!'

  return HttpResponse(message)

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
