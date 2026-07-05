from .errors import *


DOMAIN_ERROR_MAP = {
    enrollmentNotFound: (401, 'Matrícula não encontrada'),
    UserCreationError: (400, 'Erro ao criar usuário'),
    invalidName: (400, 'Nome inválido'),
    invalidPassword: (400, 'Senha inválida'),
    UserNotFoundError: (401, 'Usuário não encontrado'),
    InvitationAlreadyExistsError : (401, 'solicitação pendente'),
    InvitationNotExistsError: (401, 'so pode responder, após a direção mandar o acesso'),
    FormAlreadyExistsError: (401, 'so pode preencher 1 formulario'),
    FormNotExists: (401, 'não tem nenhum formulario com para esse aluno'),
    ClubAlreadyExistError: (401, 'ja existe um clube desse aluno'),
    DayNotValidedError: (401, 'dia invalido'),
    IsNotAdminError: (401, 'aluno não e lider de club'),
    InvalidTokenError: (401, 'token invalido, ou não fornecido'),
    IsNotManagerError: (403, 'somente a direção pode acessar essa rota')
}