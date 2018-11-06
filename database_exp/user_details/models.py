from django.db import models

# Create your models here.
class userdetails(models.Model):
    first_name=models.CharField(max_length=256,unique=True)
    last_name=models.CharField(max_length=256)
    email=models.URLField(unique=True)

    def __str__(self):
        return self.first_name

class namesAcess(models.Model):
    name= models.ForeignKey(userdetails,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
