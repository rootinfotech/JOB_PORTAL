from django.contrib import admin
from . models import Company
from . models import Applicant
from. models import Job
# Register your models here.
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['aid', 'aname', 'aphone', 'company', 'abranch','askills','ainterest','username','password']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['cid', 'cname', 'caddr', 'cdetails', 'ctype']
admin.site.register(Company,CompanyAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ['company', 'jobtitle', 'jobdesc', 'jobsalary', 'jobopno']
admin.site.register(Job,JobAdmin)
