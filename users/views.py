from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import UserForm
from .models import User


@require_http_methods(['GET'])
def index(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {'users': users})


@require_http_methods(['GET', 'POST'])
def create(request):
    form = UserForm(request.POST or None)
    if request.method == 'GET':
        return render(request, 'users/create.html', {'form': form})
    if request.method == 'POST':
        if not form.is_valid():
            return render(request, 'users/create.html', {'form': form})
        instance = form.save()
        return HttpResponseRedirect(reverse('users:update', args=[instance.pk]))
    

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    try:
        instance = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponseNotFound()
    
    form = UserForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect(reverse('users:update', args=[pk]))

    return render(request, 'users/update.html', {'form': form, 'instance': instance})
