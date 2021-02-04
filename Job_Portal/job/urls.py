from django.urls import path
from . import views

urlpatterns = [
    path('', views.Add_Company, name='addCompany'),
    path('view/', views.View_Company, name='viewCompany'),
    path('delete/', views.Delete_Company, name='deleteCompany'),
    path('edit/', views.Update_Company, name='updateCompany'),

    path('ap/', views.Add_Applicant, name='addApplicant'),
    path('view_a/', views.View_Applicant, name='viewApplicant'),
    path('adelete/', views.Delete_Applicant, name='deleteApplicant'),
    path('aedit/', views.Update_Applicant, name='updateApplicant'),

    path('job/', views.Add_Job, name='addJob'),
    path('view_j/', views.View_Job, name='viewJob'),
    path('jdelete/', views.Delete_Job, name='deleteJob'),
    path('jedit/', views.Update_Job, name='updateJob'),

    path('apply/', views.Job_apply, name='apply'),
    path('p/', views.Perticular_Company, name='company'),

    path('register/', views.Register, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout')
]