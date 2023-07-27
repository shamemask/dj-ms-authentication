from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# @sync_to_async
@login_required
def profile_view(request):
    return render(request, 'profile.html')