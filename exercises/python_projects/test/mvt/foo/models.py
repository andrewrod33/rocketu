from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=20)
    joined = models.DateField()

# class QuestionAnswers(models.Model):
#     poll = models.ForeignKey(Poll, related_name="answers")
#     answer = models.CharField(max_length=255)
#     vote_count = models.IntegerField(default=0)
#
#     def __unicode__(self):
#         return self.answer
