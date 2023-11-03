from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .validators import UnicodeUsernameIdValidator
from django.conf import settings

    

class User(AbstractUser):
    
    username_validator = UnicodeUsernameIdValidator()
    username = models.CharField(
        _("username"), max_length=12,
        unique=True,
        help_text=_(
            "Required. user id only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    
    
    def save(self, *args, **kwargs):
        if not self.pk: 
            last_username = User.objects.all().values_list('username', flat=True).last()       
            if last_username: new_username = int(last_username) + 1
            else: new_username = settings.USERID_BASE + 1
            self.username = new_username
            super(User, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.username)
    
    


    
class Profile(models.Model):
    user = models.ForeignKey("accounts.User", related_name='user', on_delete=models.CASCADE)
    phone = models.TextField(max_length=12)
    gender = models.IntegerField(choices=((1,'Male'),(2,'Female'),(3,'Others')))
    profession = models.TextField(max_length=128)
    reference = models.ForeignKey("accounts.User", related_name='referer', on_delete=models.DO_NOTHING)