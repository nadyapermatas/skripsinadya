from django.db import models

# Create your models here.

# class message (models.Model):
#     createdat = models.DateField() 
#     textField = models.CharField()
#     receiver = ForeignKey('user')
#     sender = ForeignKey('user')

class Message(models.Model):
    message_id = models.IntegerField(primary_key=True)
    message_datecreated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'
