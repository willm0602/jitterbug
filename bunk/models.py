from django.db import models
from datetime import datetime
# Create your models here.

USER_MAX_LEN = 50
IMG_URL_MAX_LEN = 200

class User(models.Model):
    username = models.CharField(max_length = USER_MAX_LEN)
    imgurl = models.CharField(max_length = IMG_URL_MAX_LEN)

    def __str__(self):
        return(self.username)

def datetimeToString(time: datetime):
    return time.strftime('%D at %H:%M')

class Bunk(models.Model):
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'sender')
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'receiver')
    sentdate = models.DateTimeField(auto_now_add = True, blank = False)

    def __str__(self):
        return("{} bunked {} on {}".format(self.sender, self.receiver, datetimeToString(self.sentdate)))
