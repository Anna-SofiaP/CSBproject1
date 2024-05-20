from django.contrib.auth import logout
from django.conf import settings
from datetime import timedelta
from django.http import HttpResponseRedirect
from django.urls import reverse

class LogoutTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.session.set_expiry(timedelta(seconds=settings.SESSION_TIMEOUT))
        #if request.user.is_authenticated and request.session.get_expiry_age():
        if request.user.is_authenticated:
            if request.session.get_expiry_age() <= 0:
                logout(request, 'myapp/login.html')
                #return HttpResponseRedirect(reverse('myapp:login'))
                #return HttpResponseRedirect(reverse('myapp:timeout'))
                #return

        response = self.get_response(request)
        return response

