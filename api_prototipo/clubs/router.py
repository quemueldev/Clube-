from ninja import Router
from clubs.services.service import ClubService
from core.errors.decorators import domain_errors
from core.auth.decorators import club_admin_required
from .schemas import *
from typing import List


router = Router()

#listar todos os clubes
@router.get('club/', response=list[ClubSchemaOut])
@domain_errors
def get_clubs(request):
    service = ClubService()
    response = service.get_clubs()
    return list(response)

@router.get('get_club/{id}', response=ClubSchemaOut)
@domain_errors
def get_club(request, id:int):
    service = ClubService()
    response = service.get_club(id)
    return response

#poder mudar a descrição
@router.patch('alter_description/')
@domain_errors
@club_admin_required
def change_description(request, data: DescriptionSchemaIn):
    service = ClubService()
    service.change_description(
        request.user.my_club,data.newDes
    )
    return{'response': 'sucesso'}

@router.patch('add_days/')
@club_admin_required
@domain_errors
def fill_days_json(request, data: DaysSchemaIn):
    service = ClubService()
    service.add_days(request.user.my_club,data.days)
    return {'response': 'sucesso'}

