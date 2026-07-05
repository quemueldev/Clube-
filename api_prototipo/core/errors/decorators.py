from ninja.errors import HttpError
from functools import wraps
from .errors import *
from .mapping import DOMAIN_ERROR_MAP

def handle_error(exc: DomainError):
    print(f"Exceção disparada: {type(exc)}")
    print(f"Existe no mapa? {type(exc) in DOMAIN_ERROR_MAP}")

    status, message = DOMAIN_ERROR_MAP.get(type(exc), (500, "Erro interno"))
    raise HttpError(status, message)
from functools import wraps

def domain_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DomainError as e:
            handle_error(e)
    return wrapper