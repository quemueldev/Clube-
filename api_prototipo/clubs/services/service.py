from clubs.models import Club
from ..infra.orm import *
from ..utils.utils import *

class ClubService:
    def __init__(self):
        pass
    def create_club(self,id, name, description):
        #chamado no manager
        student = get_user(id)
        club = Club(
            student= student,
            nome=name,
            description=description
        )
        club.save()
    def get_clubs(self):
        #tranferir para o manager
        return list_clubs()
    def get_club(self, id):
        return club(id)
    
    def change_description(self,club, newDes):
        alter_description(club,newDes)

    def add_days(self,club, list):
        for i in list:
            validate_day(i)

        add_on_db(club,list)


        