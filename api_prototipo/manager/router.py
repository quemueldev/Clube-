from ninja import Router
from core.errors.decorators import domain_errors
from core.auth.decorators import manager_required, login_required
from .services.service import ManagerService
from .schemas import *
from typing import List

router = Router()

@router.post('send_invitation/')
@domain_errors
@manager_required
def send_invitation(request, data: IdSchema):
    service = ManagerService()
    service.send_invitation(data.id)
    return {'response': 'sucesso'}

@router.post('fill_form/')
@domain_errors
#colocar isso em clubs
def form(request, data: FormSchema):
    service = ManagerService()
    service.do_form(
        data.student_id, data.name, data.description
    )
    return {'response': 'sucesso'}

@router.patch('accept_club/')
@domain_errors
@manager_required
def accept_club(request, id:int):
    service = ManagerService()
    service.accept_club(id)
    return {'response': 'sucesso'}

@router.get('test/')
@domain_errors
@manager_required
def root(request):
    print('logou sim')
    return {
        'is_superuser': request.user.is_superuser
   }

@router.get('check_manager/')
@login_required
def check_manager(request):
    return {'is_manager': request.user.is_manager}


@router.get('users/', response=List[UserResponseSchema])
@manager_required
@domain_errors
def get_users_objects(request):
    service = ManagerService()
    user_list = service.get_users()
    return user_list

@router.get('invitations/')
@domain_errors
def get_invitations(request):
    service = ManagerService()
    invitations = service.get_invitations()
    return {'invitations': invitations}