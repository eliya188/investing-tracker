from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken

def validate_token(view_func):
    def _wrapped_view(request, *args, **kwargs):
        authorization_header = request.headers.get('Authorization')
        
        if not authorization_header or not authorization_header.startswith('Bearer '):
            return JsonResponse({'error': 'Invalid authorization header.'}, status=401)

        token = authorization_header.split(' ')[1]

        try:
            refresh_token = RefreshToken(token)
            refresh_token.verify()
        except Exception as e:
            return JsonResponse({'error': 'Invalid token.'}, status=401)

        return view_func(request, *args, **kwargs)

    return _wrapped_view