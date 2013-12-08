from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from treasure_hunt.models import ObjectTip

@login_required
@require_GET
def show_tip(request, id):
    tip = ObjectTip.objects.get(id=id)
    ctx = {
        'tip_name': "Dica {0}".format(id),
        'tip_description': tip.text
    }
    
    ctx.update(csrf(request))

    return render_to_response("scan_tip.html", ctx)
