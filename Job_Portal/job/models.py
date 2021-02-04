from django.db import models
# Create your models here.

class Company(models.Model):
    cid = models.IntegerField()
    cname = models.CharField(max_length=40)
    caddr = models.CharField(max_length=50)
    cdetails = models.CharField(max_length=200)
    ctype = models.CharField(max_length=30)

    def __str__(self):
        return self.cname

class Applicant(models.Model):
    aid = models.IntegerField()
    aname = models.CharField(max_length=30)
    aphone = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    abranch = models.CharField(max_length=30)
    askills = models.CharField(max_length=60)
    ainterest = models.BooleanField(default=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)


    def __str__(self):
        return self.aname

class Job(models.Model):
    #applicant = models.ForeignKey(Applicant, null=True, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length=30)
    jobdesc = models.CharField(max_length=50)
    jobsalary = models.FloatField()
    jobopno = models.IntegerField()

    def __str__(self):
        return self.jobtitle