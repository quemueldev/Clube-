from django.db import models
from users.models import User

class ClubForm(models.Model):
    student = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('approved', 'Approved'),
            ('pending', 'Pending'),
            ('rejected', 'Rejected')
        ],default="pending"
    )

    sent_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(null=True, blank=True)

class FormInvitation(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)


"""
Direção cria Invitation (para aluno X)
↓
Invitation fica salva no banco
↓
Aluno loga
↓
Sistema verifica:
    existe Invitation para ele?
↓
Se SIM:
    libera tela do formulário
↓
Aluno envia resposta
↓
Cria ClubForm ligado à Invitation
↓
Marca como submitted / aprovado / rejeitado
"""