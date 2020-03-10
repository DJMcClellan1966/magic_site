from django.db import models
from django.contrib.auth.models import User



class Question(models.Model):
    question = models.CharField(max_length=250)
    pub_date = models.DateField()
    seeker = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.question

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
