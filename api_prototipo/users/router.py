from ninja import Router
from users.services.service import UserService
from core.errors.decorators import domain_errors
from core.auth.decorators import login_required
from .schemas import *
from django.http import HttpResponse
from ninja.errors import HttpError


router = Router()

@router.post('sign_in/')
@domain_errors
def sign_in(request, data: SingInSchema):
    service = UserService()
    service.create_user(
        data.enrollment, data.name, data.password
    )
    return {
        'response': 'User created successfully'
    }

@router.post('login/')
@domain_errors
def login(request,data: LoginSchema):
    service = UserService()
    user = service.enter(
        data.enrollment, data.password
    )
    tokens = service.get_token(user)
    return {'tokens': tokens}


@router.get('get_user/')
@domain_errors
@login_required
def show_payload(request):
    print('verificar se não explodiu dps')
    #e colocar login_required
    user = request.user
    return {
        'id': user.id,
        'enrollment': user.enrollment,
        'name': user.first_name,
        'role': user.role.capitalize()
    }

#web
@router.post('login_web/', response=LoginResponseSchema)
@domain_errors
def login_web(request,data: LoginSchema, response:HttpResponse):
    service = UserService()
    print('chegou aqui')
    user = service.enter(
        data.enrollment, data.password
    )
    access = service.set_cookies(response, user)
    return {'access_token': access}


@router.get('check_login/')
@domain_errors
@login_required
def check_login(request):
    return {'response': 'logado'}