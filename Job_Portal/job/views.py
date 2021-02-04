from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CompanyForm
from . models import Company
from . forms import ApplicantForm
from . models import Applicant
from . forms import JobForm
from . models import Job
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

@login_required()
def Add_Company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            ci = form.cleaned_data['cid']
            cn = form.cleaned_data['cname']
            cad = form.cleaned_data['caddr']
            ct = form.cleaned_data['ctype']
            cd = form.cleaned_data['cdetails']

            com = Company(cid=ci, cname=cn, caddr=cad, ctype=ct, cdetails=cd)
            com.save()
            print("company added")
            return render(request, 'job/post_job.html')
            #return redirect("/view")

    else:
        form = CompanyForm()
    template_name = 'job/comp_register.html'
    context = {'form':form}
    return render(request, template_name, context)

def View_Company(request):
    comp = Company.objects.all()
    template_name = 'job/comp_view.html'
    context = {'comps': comp}
    return render(request, template_name, context)

@login_required
def Delete_Company(request):
    id = request.GET['id']
    com = Company.objects.filter(cid=id)
    if request.method == 'GET':
        template_name = 'job/comp_delete.html'
        context = {'com':com}
        return render(request, template_name, context)

    elif request.method == 'POST':
        com = Company.objects.filter(cid=id)
        com.delete()
        return redirect("viewCompany")

@login_required
def Update_Company(request):
    id = request.GET['id']
    coms = Company.objects.get(cid=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            coms.cid = form.cleaned_data.get('cid')
            coms.cname = form.cleaned_data.get('cname')
            coms.caddr = form.cleaned_data.get('caddr')
            coms.ctype = form.cleaned_data.get('ctype')
            coms.cdetails = form.cleaned_data.get('cdetails')
            coms.save()
            return redirect('viewCompany')
        return render(request, 'job/comp_update.html', {'form':form})

    else:
        form = CompanyForm(initial={'cid':coms.cid, 'cname':coms.cname, 'caddr':coms.caddr,
                                    'ctype':coms.ctype, 'cdetails':coms.cdetails})
        template_name = 'job/comp_update.html'
        context = {'form':form}
        return render(request, template_name, context)



def Add_Applicant(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['aid']
            name = form.cleaned_data['aname']
            phone = form.cleaned_data['aphone']
            comp = form.cleaned_data['company']
            branch = form.cleaned_data['abranch']
            skill = form.cleaned_data['askills']
            interest = form.cleaned_data['ainterest']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            ap = Applicant(aid=id, aname=name, aphone=phone, company=comp, abranch=branch,
                           askills=skill, ainterest=interest, username=username, password=password)
            ap.save()
            #return redirect('/view_a')
            #return render(request, 'job/apply_job.html')
            return HttpResponse("<h3>You have successfully Applied.</h3>")

    else:
        form = ApplicantForm()
    template_name = 'job/aplicant_reg.html'
    context = {'form':form}
    return render(request, template_name, context)

def View_Applicant(request):
    appl = Applicant.objects.all()
    template_name = 'job/aplicant_view.html'
    context = {'appls': appl}
    return render(request, template_name, context)


def Delete_Applicant(request):
    id = request.GET['id']
    ap = Applicant.objects.filter(aid=id)
    if request.method == 'POST':
        ap.delete()
        return redirect('viewApplicant')
    else:
        template_name = 'job/aplicant_delete.html'
        context = {'ap':ap}
        return render(request, template_name, context)

def Update_Applicant(request):
    id = request.GET['id']
    ap = Applicant.objects.get(aid=id)
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            ap.aid = form.cleaned_data.get('aid')
            ap.aname = form.cleaned_data.get('aname')
            ap.aphone = form.cleaned_data.get('aphone')
            ap.company = form.cleaned_data.get('company')
            ap.abranch = form.cleaned_data.get('abranch')
            ap.askills = form.cleaned_data.get('askills')
            #ap.ainterest = form.cleaned_data.get('ainterest')
            ap.username = form.cleaned_data.get('username')
            ap.password = form.cleaned_data.get('password1')
            ap.save()
            return redirect('viewApplicant')
        return render(request, 'job/aplicant_update.html', {'form':form})

    else:
        form = ApplicantForm(initial={'aid':ap.aid, 'aname':ap.aname, 'aphone':ap.aphone, 'company':ap.company,
                                      'abranch':ap.abranch, 'askills':ap.askills,
                                      'username':ap.username, 'password':ap.password})
        template_name = 'job/aplicant_update.html'
        context = {'form':form}
        return render(request, template_name, context)


def Add_Job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>job added succesfully.</h3>')

    else:
        form = JobForm()
        template_name = 'job/job_add.html'
        context = {'form':form}
        return render(request, template_name, context)

def View_Job(request):
    jobs = Job.objects.all()
    template_name = 'job/job_view.html'
    context = {'jobs':jobs}
    return render(request, template_name, context)

def Delete_Job(request):
    id = request.GET['id']
    jobs = Job.objects.filter(jobtitle=id)
    if request.method == 'POST':
        jobs.delete()
        return redirect('viewJob')
    else:
        template_name = 'job/job_delete.html'
        context = {'jobs':jobs}
        return render(request, template_name, context)

def Update_Job(request):
    id = request.GET['id']
    jobs = Job.objects.get(jobtitle=id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=jobs)
        if form.is_valid():
            form.save()
            return redirect('viewJob')
        return redirect(request, 'job/job_update.html', {'form':form})

    else:
        form = JobForm(instance=jobs)
        template_name = 'job/job_update.html'
        context = {'form':form}
        return render(request, template_name, context)

def Job_apply(request):
    return render(request, 'job/apply_job.html')

def Perticular_Company(request):
    id = request.GET['id']
    comp = Company.objects.filter(cname=id)
    print(comp)
    template_name = 'job/apply_job.html'
    context = {'comps': comp}
    return render(request, template_name, context)


def Register(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse('Register successfully')
    else:
        fm = UserCreationForm()
    template_name = 'job/register.html'
    context = {'form':fm}
    return render(request, template_name, context)

def loginView(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('viewCompany')

    else:
        fm = AuthenticationForm()
    template_name = 'job/login.html'
    context = {'form':fm}
    return render(request, template_name, context)


def logoutView(request):
    logout(request)
    return redirect('/register/')
