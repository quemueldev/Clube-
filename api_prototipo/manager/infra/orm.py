from users.models import User
from core.errors.errors import *
from ..models import FormInvitation, ClubForm
from django.db import transaction
from django.shortcuts import get_list_or_404

ADMIN_ROLE = 'admin'
APPROVED_STATUS = 'approved'
def _get_user(id):
    try:
        return User.objects.get(id=id)
    except User.DoesNotExist:
        raise UserNotFoundError()
    
def _change_role_and_status(user, form):
    user.role = ADMIN_ROLE
    form.status = APPROVED_STATUS
    user.save(update_fields=['role'])
    form.save(update_fields=['status'])
    
def create_invitation(id):
    user = _get_user(id)
    if FormInvitation.objects.filter(student=user).exists():
        raise InvitationAlreadyExistsError()

    FormInvitation.objects.create(
        student=user,
    )
        
def _validate_invitation(id):
    if not FormInvitation.objects.filter(student_id = id).exists():
        raise InvitationNotExistsError()
    
def _validate_current_form(id):
    if ClubForm.objects.filter(student_id = id).exists():
        raise FormAlreadyExistsError()
def _validate_current_accept_form(id):
    status = ClubForm.objects.get(student_id = id).status
    if status == APPROVED_STATUS:
        raise ClubAlreadyExistError()
    
def fill_form(id, name, description):
    _validate_invitation(id)
    _validate_current_form(id)
    user = _get_user(id)

    ClubForm.objects.create(
        student = user,
        name = name,
        description = description,
    )


def change_status_form(id):
    student = _get_user(id)
    try:
        form = ClubForm.objects.get(student = student)
    except ClubForm.DoesNotExist:
        raise FormNotExists()
    _validate_current_accept_form(id)
    _change_role_and_status(student, form)
    return form.name, form.description

def serialized_users():
    return get_list_or_404(
        User.objects.exclude(is_superuser = True).values(
        'id', 'enrollment', 'first_name', 'role'
        )
    )
def serialized_invitations():
    return get_list_or_404(
        FormInvitation.objects.values(
        'student_id', 'student__enrollment', 'student__first_name', 'sent_at'
        )
    )
    
    