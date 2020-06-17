from django.db import models

# Create your models here.
class Message(models.Model):
	name=models.CharField(max_length=20,null=True)
	prefix=models.CharField(max_length=20,null=True)
	ipaddress=models.CharField(max_length=100,null=True)

