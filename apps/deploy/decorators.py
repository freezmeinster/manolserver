import base64
from django.contrib.auth import authenticate
from django.shortcuts import HttpResponse

def basic_auth_required(view_func):
        def _wrapped_view_func(request, *args, **kwargs):
            if 'HTTP_AUTHORIZATION' in request.META:
                auth = request.META['HTTP_AUTHORIZATION'].split()
                if len(auth) == 2:
                    if auth[0].lower() == "basic":
                        uname, passwd = base64.b64decode(auth[1]).split(':')
                        user = authenticate(username=uname, password=passwd)
                        if user is not None and user.is_active:
                            request.user = user
                            return view_func(request, *args, **kwargs)
                        else:
                            return HttpResponse("INVALID USER")
                    else:
                        return HttpResponse("NOT BASIC AUTH")
                else:
                    return HttpResponse("BASIC AUTH ERROR")
            else:
                return HttpResponse("AUTH ERROR")
        return _wrapped_view_func