
from users.utils.utils import *
from users.infra.orm import *
from users.infra.auth import *

from ninja.responses import Response
from django.http import HttpResponse
from django.conf import settings

class UserService:
    def __init__(self):
        pass
    def create_user(self, enrollment, name, password):
        validate_credentials(enrollment, name, password)
        create_user(enrollment, name, password)

    def enter(self, enrollment, password):
        return get_user(enrollment, password)
    
    def get_token(self,user):
        return generate_tokens(user)
    
    def set_cookies(self,response, user):
        print("ENTROU LOGIN")

        tokens = generate_tokens(user)
        print("TOKEN GERADO")

        response.set_cookie(
            "refresh_token",
            tokens['refresh'],
            httponly=True,
            secure=False,
            samesite="Lax",
            max_age=60 * 60 * 24 * 7,
        )

        print("COOKIE SETADO")

        return tokens['access']