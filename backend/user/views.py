from django.http import HttpResponse ,JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt    
from django.shortcuts import get_object_or_404 
from rest_framework import status 
from .models import Profile
from django.views.decorators.http import require_http_methods
import json

@require_http_methods(['POST'])
@csrf_exempt
def registration(request):
    user_data = json.loads(request.body)
    profile = Profile.objects.create()
    if profile.clean(user_data):
        user = User.objects.create_user(username=user_data.get("username"), email=user_data.get("email"), password=user_data.get("password"))
        profile.user = user
        profile.save()
        return HttpResponse(request, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(request, status=status.HTTP_400_BAD_REQUEST)
    
@require_http_methods(['PUT'])
@csrf_exempt
def change_password(request):
    user_data = json.loads(request.body)
    user = get_object_or_404(User, pk = user_data.get("username"), password = user_data.get("password"))
    return JsonResponse(user, status = status.HTTP_202_ACCEPTED)
    


    
@require_http_methods(['DELETE'])
@csrf_exempt
def remove_user(request, user_id):
    user_to_delete = get_object_or_404(User, pk = user_id)
    user_to_delete.delete()
    return HttpResponse(request, status = status.HTTP_200_OK)