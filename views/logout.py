from urllib import request

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def logout(request_in: request):
    if request_in.session.get('user_id'):
        del request_in.session['user_id']
        del request_in.session['user_email']
        del request_in.session['user_primary_email']
    if request_in.user:
        del request_in.user
        request_in.session.save()

    return redirect('index')