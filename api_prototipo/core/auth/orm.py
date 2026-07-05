from users.models import User
from ..errors.errors import *

def user_from_id(id) -> User:
    try:
        return User.objects.get(id=id)
    except User.DoesNotExist:
        raise UserNotFoundError()