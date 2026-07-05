import os
from core.errors.errors import *


def _validate_enrollment(enrollment) -> bool:
    enrollments = os.getenv('MATRICULAS').split(',')
    if enrollment not in enrollments:
        raise enrollmentNotFound()
    
def _validate_name(name):
    if not name:
        raise invalidName()
    if len(name) < 3:
        raise invalidName()
    
def _validate_password(password):
    if not password:
        raise invalidPassword()
    if len(password) < 6:
        raise invalidPassword()
    
def validate_credentials(enroll, name, password):
    _validate_enrollment(enroll)
    _validate_name(name)
    _validate_password(password)
    
def get_token_from_bearer(token_bearer):
    return token_bearer.split(' ')[1]

