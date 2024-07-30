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
    path('change_password', views.change_password, name='change_password'),
    path('logout', views.logout_user, name='logout'),
    path('adminpanel', views.adminPanel, name='adminpanel'),
    path('users', views.users, name='users'),
    path('change_password_admin', views.change_password_admin, name='change_password_admin'),
    path('delete_user/<int:pid>', views.delete_user, name='delete_user'),
    path('update_education_admin/<int:pid>', views.update_education_admin, name='update_education_admin'),
    path('update_career_admin/<int:pid>', views.update_career_admin, name='update_career_admin'),
    path('add_user_admin', views.add_user_admin, name='add_user_admin'),
]