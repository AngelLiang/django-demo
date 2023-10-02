from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user
    return render(request, 'user_profile/profile.html', {'user': user})
