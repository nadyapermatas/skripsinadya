from django.db import models

# Create your models here.

class User(models.Model):
    user_firstname = models.CharField(max_length=200)
    user_id = models.IntegerField(primary_key=True)
    user_lastname = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'user'

class GroupUser(models.Model):
    group_user_id = models.IntegerField(primary_key=True)
    group_user_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'group_user'

class UserRole(models.Model):

    ADMINISTRATOR = 1
    MAHASISWA = 2
    SCAC= 3

    """ Model for user profile status """
    name = models.CharField(max_length=32, default='')

    class Meta:
        db_table = "accounts_userprofile_role"

def __str__(self):
        return self.name

class UserProfile(models.Model):
    """ Model to represent additional information about user """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(
        max_length=2000,
        blank=True,
        default=''
    )
    # we use URL instead of imagefield because we'll use 3rd party img hosting later on
    avatar = models.URLField(default='', blank=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, default='')
    
#  return self.user.username


