from ninja_jwt.tokens import RefreshToken
from ..errors.errors import *
from ninja.errors import HttpError

def _validate_bearer(auth_header):
    if not auth_header:
        raise InvalidTokenError()
    
    if auth_header.startswith("Bearer "):
        return auth_header.split(' ')[1]
    return auth_header

def get_user_id(token) :
    try:
        refresh = RefreshToken(token)
        return refresh.payload['user_id']
    except Exception:
        raise InvalidTokenError()

def get_refresh_token(request):
    web_token = request.COOKIES.get('refresh_token')
    if web_token:
        return web_token

    auth = request.headers.get("Authorization")
    return _validate_bearer(auth)
    
   

    