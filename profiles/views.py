from django.shortcuts import render
from .models import Profile
from django.shortcuts import render
from .forms import ProfileModelForm

def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm()
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'obj': profile,
        'form': form,
        'confirm': confirm,
    }

    return render(request, 'profiles/myprofile.html', context)