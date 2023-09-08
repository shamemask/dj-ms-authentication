from urllib import request

from django.shortcuts import redirect


def logout(request_in: request):
    if request_in.session.get('user_id'):
        del request_in.session['user_id']
        del request_in.session['user_email']
        del request_in.session['user_primary_email']
    return redirect('index')