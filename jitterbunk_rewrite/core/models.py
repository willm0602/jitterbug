from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, default="", null=False)
    img = models.CharField(max_length=255, default="", null=False)

class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete = models.CASCADE, null=False, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete = models.CASCADE, null=False, related_name='to_user')
    date = models.DateField(auto_now_add=True, null=False)