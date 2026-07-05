from ..infra.orm import *
from clubs.services.service import ClubService


class ManagerService:
    def __init__(self):
        pass
    def send_invitation(self, id):
        create_invitation(id)
        
    def do_form(self, id, name, description):
        fill_form(id, name, description)

    def accept_club(self, id):
        name, description = change_status_form(id)
        service = ClubService()
        service.create_club(id, name, description)

    def get_users(self):
        return serialized_users()
    
    def get_invitations(self):
        return serialized_invitations()