from django import forms
from django.forms import modelformset_factory
from .models import *


class EmployeeEducationForm(forms.ModelForm):
    class Meta:
        model = EmployeeEducation
        fields = ['degree', 'institute', 'passing_year', 'score']


EmployeeEducationFormSet = modelformset_factory(
    EmployeeEducation,
    form=EmployeeEducationForm,
    extra=1,
    can_delete=True
)


class EmployeeCareerForm(forms.ModelForm):
    class Meta:
        model = EmployeeCareer
        fields = ['company', 'designation', 'joining_date', 'leaving_date']


EmployeeCareerFormSet = modelformset_factory(
    EmployeeCareer,
    form=EmployeeCareerForm,
    extra=1,
    can_delete=True
)
