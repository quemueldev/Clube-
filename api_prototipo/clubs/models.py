from django.db import models
from users.models import User

DAY_CHOICES = [
    ("MON", "Segunda"),
    ("TUE", "Terça"),
    ("WED", "Quarta"),
    ("THU", "Quinta"),
    ("FRI", "Sexta"),
]

class Club(models.Model):
    student = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='my_club'
    )
    name = models.CharField(max_length=60) #trocar para title
    description = models.TextField()
    activity_days = models.JSONField(
        default=list,
        blank=True
        #salvar como se fosse eu lista -> ['segunda', 'terça']
    )
    """
    os dias tem que ser validos:
     fazer uma lista no utils e ver 
     se a resposta e valida entre os dias 
     da lista e no front eu faço o aluno escolher 
     o dia atraves de uma caixinha assim o dia 
     vai vir escrito sempre do mesmo jeito e eu 
     valido so para não explodir em caso de hacker
    """
    created_at = models.DateTimeField(auto_now_add=True)


    #admin
    def __str__(self):
        return self.name
    
class ClubPhoto(models.Model):
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    image = models.ImageField(
        upload_to="club_photos/"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo {self.id} - {self.club.name}"