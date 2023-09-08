from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import CustomerForm
from .models import Customer

# Create your views here.
require_http_methods(['GET', 'POST'])
def create_customer(request):
    form = CustomerForm(data=request.POST or None)
    if request.method == 'GET':
        return render(request, 'customers/create.html', {'form': form})
    if request.method == 'POST':
        if not form.is_valid():
            return render(request, 'customers/create.html', {'form': form})
        instance = form.save()
        return HttpResponseRedirect(reverse('customer-update', args=[instance.pk]))
    

@require_http_methods(['GET', 'POST'])
def update_customer(request, pk):
    try:
        instance = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponseNotFound()
    
    form = CustomerForm(data=request.POST or None, instance=instance)

    if request.method == 'GET':
        return render(request, 'customers/update.html', {'customer': instance, 'form': form})
    
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()
        return render(request, 'customers/update.html', {'customer': instance, 'form': form})
