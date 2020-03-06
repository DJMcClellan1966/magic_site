from django.db import models

class CelticCross(models.Model):
    question = models.CharField(max_length=250)
    pub_date = models.DateField()
    cover = models.ImageField(upload_to='images/')
    crossing = models.ImageField(upload_to='images/')
    foundation = models.ImageField(upload_to='images/')
    behind = models.ImageField(upload_to='images/')
    crowning = models.ImageField(upload_to='images/')
    before = models.ImageField(upload_to='images/')
    feelings = models.ImageField(upload_to='images/')
    opinions = models.ImageField(upload_to='images/')
    hopes = models.ImageField(upload_to='images/')
    outcome = models.ImageField(upload_to='images/')
    answer = models.TextField()

    def summary(self):
        return self.question[:100]

    def __str__(self):
        return self.question
