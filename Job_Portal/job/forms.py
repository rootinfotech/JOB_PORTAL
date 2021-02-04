from django import forms
from django.core import validators
from .models import Job
from .models import Company, Applicant
branch_choices = (
    ('Aeronautical', 'Aeronautical'),
    ('Mechanical', 'mechanical'),
    ('Electrical', 'Electrical'),
    ('civil', 'Civil'),
    ('IT', 'IT'),
    ('Computer', 'Computer'),
)
INTEREST_CHOICES = [('programming', 'Programming'),
                    ('dancing', 'Dancing'),
                    ('singing', 'Singing'),
                    ('gaming', 'Gaming'),
                    ('sports', 'Sports')]

def cname_validator(n):
    if not n.isalpha():
        raise forms.ValidationError("username should not contain numeric & special Character")

class CompanyForm(forms.Form):
    cid = forms.IntegerField(label='Enter Company ID')
    cname = forms.CharField(label='Enter Company Name', validators=[cname_validator])
    caddr = forms.CharField(label='Enter Company Address')
    cdetails = forms.CharField(label='Enter Company Details')
    ctype = forms.CharField(label='Enter Company Type')

class ApplicantForm(forms.Form):
    aid = forms.IntegerField(label='Enter Applicant ID')
    aname = forms.CharField(label='Enter Applicant Name')
    aphone = forms.CharField(label='Enter Applicant Mobile no', validators=[validators.MaxLengthValidator(10)])
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    abranch = forms.CharField(label='Enter Specialization', widget=forms.Select(choices=branch_choices))
    askills = forms.CharField(label='Enter Applicants skills')
    ainterest = forms.MultipleChoiceField(label="Enter Applicants Interest", required=False,
                                          widget=forms.CheckboxSelectMultiple,
                                          choices=INTEREST_CHOICES,
                                       )
    username = forms.CharField(label='Enter Username')
    password1 = forms.CharField(label='Enter Password', validators=[validators.MaxLengthValidator(8)],
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean(self):
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']
        p = self.cleaned_data['aid']
        print(p)
        if p1 != p2 :
            raise forms.ValidationError("password doesnt matched")

        entered_password1 = self.cleaned_data['password1']
        if entered_password1.islower():
            raise forms.ValidationError("password should not be in lowercase")
        if entered_password1.isupper():
            raise forms.ValidationError("password should not be in Uppercase")
        if not any([True for x in entered_password1 if x.isdigit()]):
            raise forms.ValidationError("password should contain some numbers")
        l = ['@', '#', '|', '_', '$']
        if not any([True for x in entered_password1 if x in l]):
            raise forms.ValidationError("password should have one special character")

        entered_username = self.cleaned_data['username']
        if entered_username.islower():
            raise forms.ValidationError("username should not be in lowercase")
        if entered_username.isupper():
            raise forms.ValidationError("username should not be in Uppercase")
        if not any([True for x in entered_username if x.isdigit()]):
            raise forms.ValidationError("username should contain some numbers")
        l = ['@', '#', '|', '_', '$']
        if not any([True for x in entered_username if x in l]):
        #if '@' not in entered_username or '#' not in entered_username or '$' not in entered_username:
            raise forms.ValidationError("username should have one special character")


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


