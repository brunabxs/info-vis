# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_POST, require_GET
from django.core.context_processors import csrf

@require_POST
def login(request):
  valid = validate_user(username=request.POST['name'], password=request.POST['password'])

  return HttpResponse(valid)

@require_GET
def home(request):
  c = {}
  c.update(csrf(request))
  return render_to_response("index.html", c)

def new_user(request):
  from caca_ao_tesouro.models.user import User


def validate_user(username, password):
  from django.contrib.auth.models import User

  if User.objects.filter(username=username, password=password):
    return True
  else:
    return False
