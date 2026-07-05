from .rules import *
from .orm import *
from ..errors.errors import *
from functools import wraps
# @wraps é para copiar info da func original
# sem ele o django tenta enxergar func(request,id,data)
# e enxerga wrapper(*args, *kargs)


def login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        token = get_refresh_token(request)
        user_id = get_user_id(token)
        request.user = user_from_id(user_id)

        return func(request, *args, **kwargs)

    return wrapper


def club_admin_required(func):
    @login_required
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.role != "admin":
            raise IsNotAdminError()
        return func(request, *args, **kwargs)

    return wrapper


def manager_required(fn):
    @login_required
    @wraps(fn)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise IsNotManagerError()
        return fn(request, *args, **kwargs) 
    return wrapper