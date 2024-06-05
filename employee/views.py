from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def registration(request):
    error = ''
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        emp_code = request.POST['emp_code']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=f'{first_name} {last_name[:1]}-'.title() + str(emp_code),
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email,
                                            password=password)
            EmployeeDetails.objects.create(user=user, employee_id=emp_code)
            error = 'no'
        except:
            error = 'yes'
    return render(request, 'registration.html', {'error': error})


def employeelogin(request):
    error = ''
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            username = User.objects.filter(email=email).first().username
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    return render(request, 'employeelogin.html', {'error': error})


def adminlogin(request):
    return render(request, 'adminlogin.html')


def logout_user(request):
    logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated is False:
        return redirect('employeelogin')
    return render(request, 'emp/emp_dash.html')


def profile(request):
    error = ''
    user = request.user
    employee = EmployeeDetails.objects.filter(user=user).first()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        emp_code = request.POST['emp_code']
        email = request.POST['email']
        username = request.POST['username']
        contacts = request.POST['contacts']
        dept = request.POST['department']
        gender = request.POST['gender']
        joining_date = request.POST['join_date']
        birth_date = request.POST['dob']
        try:
            employee.user.first_name = first_name
            employee.user.last_name = last_name
            employee.user.email = email
            employee.user.username = username
            employee.employee_id = emp_code
            employee.contacts = contacts
            employee.employee_dept = dept
            employee.gender = gender
            employee.joining_date = joining_date
            employee.birth_date = birth_date

            employee.user.save()
            employee.save()
            print(employee)
            error = 'no'
        except:
            error = 'yes'
    return render(request, 'emp/profile.html', {'employee': employee, 'error': error})


def education(request):
    error = ''
    user = request.user
    education = EmployeeEducation.objects.filter(user=user)
    return render(request, 'emp/education.html', {'education': education, 'error': error})


def edit_education(request):
    user = request.user
    error = ''
    if request.method == 'POST':
        formset = EmployeeEducationFormSet(request.POST, request.FILES,
                                           queryset=EmployeeEducation.objects.filter(user=user))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = user
                instance.save()
            formset.save_m2m()
            return redirect('edit_education')
    else:
        formset = EmployeeEducationFormSet(queryset=EmployeeEducation.objects.filter(user=user))

    return render(request, 'emp/edit_education.html', {'formset': formset, 'error': error})


def career(request):
    return render(request, 'emp/career.html')


def edit_career(request):
    return render(request, 'emp/edit_career.html')
