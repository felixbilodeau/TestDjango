from django.db import models

# Create your models here.
class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name
