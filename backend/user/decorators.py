from django.http import JsonResponse
from rest_framework.exceptions import AuthenticationFailed
import jwt

def validate_token(view_func):
    def _wrapped_view(request, *args, **kwargs):
        token = request.COOKIES.get('jwt')
    
        if not token:
            raise AuthenticationFailed("Unautenticated")
        
        try:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
            user_id = payload['id']
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unautenticated")
        # try:
        #     refresh_token = RefreshToken(token)
        #     refresh_token.verify()
        # except Exception as e:
        #     return JsonResponse({'error': 'Invalid token.'}, status=401)

        return view_func(request, user_id, *args, **kwargs)

    return _wrapped_view