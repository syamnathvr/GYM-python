from django.db import models

class userdata(models.Model):
    userphoto=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    useremail=models.CharField(max_length=200)
    userpass=models.CharField(max_length=200)


class staffdetails(models.Model):
    staffphoto=models.CharField(max_length=200)
    staffname=models.CharField(max_length=200)
    staffspec=models.CharField(max_length=300)

class eqdetails(models.Model):
    eqphoto=models.CharField(max_length=200)
    eqname=models.CharField(max_length=200)

class classdetails(models.Model):
    staffnames=models.CharField(max_length=200)
    staffspecs=models.CharField(max_length=200)
    classtime=models.CharField(max_length=100)
    classdate=models.CharField(max_length=30)
    
class enrollclass(models.Model):
    userid=models.IntegerField()
    staffnames=models.CharField(max_length=200)
    staffspecs=models.CharField(max_length=200)
    classtime=models.CharField(max_length=100)
    classdate=models.CharField(max_length=30)


class feedbacks(models.Model):
    userid=models.IntegerField()
    feedback=models.CharField(max_length=500)

class eqbook(models.Model):
    userid=models.IntegerField()
    eqnames=models.CharField(max_length=200)
    classtime=models.CharField(max_length=100)            