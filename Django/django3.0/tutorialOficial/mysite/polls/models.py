################################################################################
import datetime

from django.db import models
from django.utils import timezone
################################################################################
# Create your models here.

################################################################################
class Question(models.Model):
    """
    El modelo Question establece que una cuestion va a tener una pregunta
    y una fecha de publicacion
    """
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        """
        Esta funcion al utilizarla mediante el shell, devuelve True
        si la fecha es cercana a la fecha presente.
        """
        now = timezone.now()
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return '%s %s %s' %(self.id, self.question_text, self.pub_date)

################################################################################

################################################################################
class Choice(models.Model):
    """
    El modelo Choice establece que una Choice tendra una pregunta
    la cual se vincula con el modelo Question por medio de su ID
    tendra tambien una opcion y un numero de votos
    """
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s %s' %(self.id, self.choice_text, self.votes)
################################################################################
