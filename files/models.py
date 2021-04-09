from django.db import models

# Create your models here.

class Files(models.Model):
    files_name = models.CharField(max_length=200)
    files_id = models.IntegerField(primary_key=True)
    files_createat = models.DateTimeField()

    class Meta:
        db_table = 'files'

    def __str(self):
        return "{}".format(self.name)


