from django import forms
from django.forms import ValidationError

from .models import Customer


class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=250)
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

    def __init__(self, *args, instance=None, **kwargs):
        if kwargs.get('data') is None and instance is not None:
            kwargs['initial'] = {
                'first_name': instance.first_name,
                'last_name': instance.last_name,
                'email': instance.email,
                'username': instance.username,
                'password': instance.password,
            }
        super().__init__(*args, **kwargs)
        self.instance = instance

    def save(self, commit=True):
        if not hasattr(self, 'cleaned_data'):
            raise ValidationError('Form is not validated yet!')

        if self.instance is not None:
            instance = self.instance
            for key, value in self.cleaned_data.items():
                setattr(instance, key, value)
        else:
            instance = Customer(**self.cleaned_data)
            self.instance = instance

        if commit:
            instance.save()

        return instance