from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Published date')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chooice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    

# Create your models here.
