from django.shortcuts import render
from .models import Profile
from django.shortcuts import render
from .forms import ProfileModelForm

def my_profile_view(request):
    obj = Profile.objects.get(user=request.user)

    context = {
        'obj': obj
    }

    return render(request, 'profiles/myprofile.html', context)