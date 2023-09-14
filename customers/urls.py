from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_customer, name='create'),
    path('<int:pk>/', views.update_customer, name='update'),
]
