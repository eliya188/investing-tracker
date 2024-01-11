from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('check' , remove_user, name='check')
    # path("remove-user/<int:user_id>", views.remove_user, name='remove'),
    # path("change-password/", views.change_password, name='change-password'),
]