from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/' , include('user.urls')),
    path('investment/', include('investment.urls')),
]
