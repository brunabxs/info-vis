from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required

@login_required
@require_GET
def show_tip(request, id):
	return HttpResponse("Detalhe da Dica {0}!".format(id))