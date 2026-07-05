from ..models import User
from core.errors.errors import *

def create_user(enrollment, name, password):
    try:
        user = User.objects.create_user(
            enrollment=enrollment, 
            first_name=name, 
            password=password
            )
    except Exception as e:
        raise UserCreationError("Error creating user")
    
def get_user(enrollment, password):
    try:
        user = User.objects.get(
            enrollment=enrollment
        )

        if not user.check_password(password):
            raise UserNotFoundError()

        return user

    except User.DoesNotExist:
        raise UserNotFoundError()
    
def user_from_id(id) -> User:
    try:
        return User.objects.get(id=id)
    except User.DoesNotExist:
        raise UserNotFoundError()