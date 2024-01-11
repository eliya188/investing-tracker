from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt    
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serilaizers import ProfileSerializers
from .models import Profile

from .decorators import validate_token
import jwt, datetime


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return JsonResponse({'error': 'Username, email, and password are required.'}, status=400)
    serialized_data= ProfileSerializers(data=request.data) 

    if serialized_data.is_valid(): 
        user = Profile.objects.create_user(username=username, email=email, password=password)
        user_serializer = ProfileSerializers(user)

        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return JsonResponse({'user': user_serializer.data, 'tokens': tokens}, status=201)
    return HttpResponse(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return JsonResponse({'error': 'Username and password are required.'}, status=400)

    user = authenticate(request, username=username, password=password)

    if user is not None:

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = HttpResponse("sign in", status=status.HTTP_200_OK)

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response
    else:
        return JsonResponse({'error': 'Invalid credentials.'}, status=401, safe=False)
    
    
@api_view(['GET'])
def remove_user(request):
    token = request.COOKIES.get('jwt')
    
    if not token:
        raise AuthenticationFailed("Unautenticated")
    
    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unautenticated")

    print(payload['id'])
    user = Profile.objects.filter(id=payload['id'])
    serializer = ProfileSerializers(user)
    print(serializer.data)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)