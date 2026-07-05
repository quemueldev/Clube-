class DomainError(Exception):
    """Erro base do domínio"""
    pass
class enrollmentNotFound(DomainError):
    pass
class UserCreationError(DomainError):
    pass
class invalidName(DomainError):
    pass
class invalidPassword(DomainError):
    pass
class UserNotFoundError(DomainError):
    pass
class InvitationAlreadyExistsError(DomainError):
    pass
class InvitationNotExistsError(DomainError):
    pass
class FormAlreadyExistsError(DomainError):
    pass
class FormNotExists(DomainError):
    pass
class ClubAlreadyExistError(DomainError):
    pass
class DayNotValidedError(DomainError):
    pass
class IsNotAdminError(DomainError):
    pass
class InvalidTokenError(DomainError):
    pass
class IsNotManagerError(DomainError):
    pass