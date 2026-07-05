from core.errors.errors import *

DAYS_PERMITED = [
    'segunda', 'terca', 'quarta', 'quinta', 'sexta'
]
def validate_day(day):
    if not day in DAYS_PERMITED:
        raise DayNotValidedError()