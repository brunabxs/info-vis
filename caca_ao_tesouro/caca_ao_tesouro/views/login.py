# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_POST, require_GET
from django.core.context_processors import csrf

from caca_ao_tesouro.models import User

@require_POST
def login(request):
  valid = User.validate_user(name=request.POST['name'], password=request.POST['password'])

  return HttpResponse(valid)

@require_GET
def home(request):
  c = {}
  c.update(csrf(request))
  return render_to_response("index.html", c)

def new_user(request):
  from caca_ao_tesouro.models.user import User
