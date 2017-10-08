from django.shortcuts import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from deploy.models import DeployPlan
from deploy.decorators import basic_auth_required

@basic_auth_required
def deploy(request, code, key):
    try:
        plan = DeployPlan.objects.get(code=code,
                                      auth_key=key,
                                      is_active=True)
        plan.deploy()
        return HttpResponse("DEPLOYED")
    except ObjectDoesNotExist:
        return HttpResponse("NOT EXIST")