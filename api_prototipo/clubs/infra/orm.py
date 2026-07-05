from users.models import User
from ..models import Club
from core.errors.errors import *
from django.http import Http404

def get_user(id):
    try:
        return User.objects.get(id=id)
    except User.DoesNotExist:
        raise UserNotFoundError()
    
def list_clubs():
    return Club.objects.select_related('student').all()
"""
        'id',
        'student',
        'name',
        'description',
        'activity_days',
        'created_at'
"""        
def club(id):
    try:
        return Club.objects.get(id=id)
    except Club.DoesNotExist:
        raise Http404('não tem clubes com esse id')

    
def alter_description(club,newDes):
    club.description = newDes
    club.save()

def add_on_db(club,list):
    club.activity_days = list
    club.save()
    
