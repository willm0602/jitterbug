from django.db import models

# Create your models here.

USER_MAX_LEN = 50
IMG_URL_MAX_LEN = 200

class User(models.Model):
    username = models.CharField(max_length = USER_MAX_LEN)
    imgurl = models.CharField(max_length = IMG_URL_MAX_LEN)

    def __str__(self):
        return(self.username)

class Bunk(models.Model):
    
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'sender')
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'receiver')
    sentdate = models.DateField()

    def __str__(self):
        return("From {} To {} on {}".format(self.sender, self.receiver, self.sentdate))
    