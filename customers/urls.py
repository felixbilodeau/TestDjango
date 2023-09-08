from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.create_customer, name='customer-create'),
    path('<int:pk>/update/', views.update_customer, name='customer-update'),
]