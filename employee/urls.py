from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about-us'),
    path('registration', views.registration, name='registration'),
    path('employeelogin', views.employeelogin, name='employeelogin'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('education', views.education, name='education'),
    path('edit_education', views.edit_education, name='edit_education'),
    path('career', views.career, name='career'),
    path('edit_career', views.edit_career, name='edit_career'),
    path('logout', views.logout_user, name='logout'),
]