from django.db import models
class Client(models.Model):
    name=models.CharField(max_length=40)
    location=models.IntegerField(null=True)

class Driver(models.Model):
    name=models.CharField(max_length=40)
    status=models.IntegerField(default=0)

class Store(models.Model):
    name=models.CharField(max_length=40)
    status=models.IntegerField()
    location=models.IntegerField(null=True)

class Items(models.Model):
    name=models.CharField(max_length=40)
    store=models.ForeignKey(Store,on_delete=models.CASCADE)
    price=models.IntegerField()

class CMD (models.Model):
    id=models.AutoField(primary_key=True)
    driver=models.ForeignKey(Driver,on_delete=models.SET_NULL,null=True)
    client=models.ForeignKey(Client,on_delete=models.CASCADE,null=True)
    store=models.ForeignKey(Store,on_delete=models.CASCADE)
    status=models.SmallIntegerField()
    total=models.IntegerField(default=0)

class CMD_line(models.Model):
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    cmd=models.ForeignKey(CMD,on_delete=models.CASCADE)
# Create your models here