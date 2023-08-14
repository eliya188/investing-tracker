from django.urls import path
from . import views

urlpatterns = [
    path("registerion/", views.registration, name='register'),
    path("remove-user/<int:user_id>", views.remove_user, name='remove'),
    path("change-password/", views.change_password, name='change-password'),
]