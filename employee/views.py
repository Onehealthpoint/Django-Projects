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
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email,
                                            password=password)
            emp_code = getEmpCode()
            EmployeeDetails.objects.create(user=user, employee_id=emp_code)
            error = 'no'
        except:
            error = 'yes'
    return render(request, 'registration.html', {'error': error})


def getEmpCode():
    start = 1000
    emp_codes = sorted([int(i.employee_id) for i in EmployeeDetails.objects.all()])
    if len(emp_codes) == 0:
        return start
    if len(emp_codes) != emp_codes[-1]:
        for i in range(start, emp_codes[-1]):
            if i not in emp_codes:
                return i
    return emp_codes[-1] + 1


def employeelogin(request):
    error = ''
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    return render(request, 'employeelogin.html', {'error': error})


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
    user = request.user
    education = EmployeeEducation.objects.filter(user=user)
    return render(request, 'emp/education.html', {'education': education, 'length_of_formset': len(education)})


def change_password(request):
    error = ''
    user = request.user

    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            if user.check_password(current_password):
                user.set_password(new_password)
                user.save()
                error = 'no'
                return redirect('employeelogin')
            else:
                error = 'yes'
        except:
            error = 'yes'
    return render(request, 'emp/change_password.html', locals())


def edit_education(request):
    error = ''
    user = request.user
    if request.method == 'POST':
        formset = EmployeeEducationFormSet(request.POST, queryset=EmployeeEducation.objects.filter(user=user))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = user
                instance.save()
            for obj in formset.deleted_objects:
                obj.delete()
            return redirect('edit_education')
    else:
        formset = EmployeeEducationFormSet(queryset=EmployeeEducation.objects.filter(user=user))

    return render(request, 'emp/edit_education.html', {'formset': formset})


def career(request):
    user = request.user
    careers = EmployeeCareer.objects.filter(user=user)
    return render(request, 'emp/career.html', {'careers': careers, 'length_of_formset': len(careers)})


def edit_career(request):
    error = ''
    user = request.user
    if request.method == 'POST':
        formset = EmployeeCareerFormSet(request.POST, queryset=EmployeeCareer.objects.filter(user=user))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = user
                instance.save()
            for obj in formset.deleted_objects:
                obj.delete()
            return redirect('edit_career')
    else:
        formset = EmployeeCareerFormSet(queryset=EmployeeCareer.objects.filter(user=user))

    return render(request, 'emp/edit_career.html', {'formset': formset})


def adminlogin(request):
    error = ''
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user.is_staff:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    return render(request, 'adminlogin.html', {'error': error})


def adminPanel(request):
    if request.user.is_authenticated is False:
        return redirect('adminlogin')
    return render(request, 'admin/adminpanel.html')


def users(request):
    if request.user.is_authenticated is False:
        return redirect('adminlogin')
    users = EmployeeDetails.objects.all()
    return render(request, 'admin/users.html', locals())


def change_password_admin(request):
    if not request.user.is_authenticated:
        return redirect('index')

    error = ''
    user = request.user

    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            if user.check_password(current_password):
                user.set_password(new_password)
                user.save()
                error = 'no'
                return redirect('adminlogin')
            else:
                error = 'yes'
        except:
            error = 'yes'
    return render(request, 'admin/change_password.html', locals())


def delete_user(request, pid):
    if request.user.is_authenticated is False:
        return redirect('adminlogin')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('users')


def update_education_admin(request, pid):
    if request.user.is_authenticated is False:
        return redirect('adminlogin')
    user = User.objects.get(id=pid)
    if request.method == 'POST':
        formset = EmployeeEducationFormSet(request.POST, queryset=EmployeeEducation.objects.filter(user=user))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = user
                instance.save()
            for obj in formset.deleted_objects:
                obj.delete()
            return redirect('update_education_admin', pid=pid)
    else:
        formset = EmployeeEducationFormSet(queryset=EmployeeEducation.objects.filter(user=user))
    return render(request, 'admin/update_education_admin.html', locals())


def update_career_admin(request, pid):
    if request.user.is_authenticated is False:
        return redirect('adminlogin')
    user = User.objects.get(id=pid)
    if request.method == 'POST':
        formset = EmployeeCareerFormSet(request.POST, queryset=EmployeeCareer.objects.filter(user=user))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = user
                instance.save()
            for obj in formset.deleted_objects:
                obj.delete()
            return redirect('update_career_admin', pid=pid)
    else:
        formset = EmployeeCareerFormSet(queryset=EmployeeCareer.objects.filter(user=user))
    return render(request, 'admin/update_career_admin.html', locals())


def add_user_admin(request):
    if request.user.is_authenticated is False:
        return redirect('adminlogin')
    error = ''
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email,
                                            password=password)
            emp_code = getEmpCode()
            EmployeeDetails.objects.create(user=user, employee_id=emp_code)
            error = 'no'
        except:
            error = 'yes'
    return render(request, 'admin/add_user_admin.html', {'error': error})