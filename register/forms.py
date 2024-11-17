from django import forms
from . import models

class CreateCountry(forms.ModelForm):
    class Meta:
        model = models.Country
        fields = "__all__"

class EraseCountry(forms.CharField):
    class Meta:
        model = models.Country
        fields = ['u_email']

class UpdateCountry(forms.ModelForm):
    class Meta:
        model = models.Country
        fields = "__all__"

        label = {
        "u_email" : "Email",
        "u_name" : "Name",
        "u_surname" : "Surname",
        "u_salary" : "Salary",
        "u_phone" : "Phone",
        "u_cname" : "Country",
        }


class CreateDT(forms.ModelForm):
    class Meta:
        model = models.DiseaseType
        fields = "__all__"





class EraseDT(forms.CharField):
    class Meta:
        model = models.DiseaseType
        fields = ['u_email']

class UpdateDT(forms.ModelForm):
    class Meta:
        model = models.DiseaseType
        fields = "__all__"

        label = {
        "u_email" : "Email",
        "u_name" : "Name",
        "u_surname" : "Surname",
        "u_salary" : "Salary",
        "u_phone" : "Phone",
        "u_cname" : "Country",
        }

class CreateUser(forms.ModelForm):
    class Meta:
        model = models.Users
        fields = "__all__"

class EraseUser(forms.CharField):
    class Meta:
        model = models.Users
        fields = ['u_email']

class UpdateUser(forms.ModelForm):
    class Meta:
        model = models.Users
        fields = "__all__"

        label = {
        "u_email" : "Email",
        "u_name" : "Name",
        "u_surname" : "Surname",
        "u_salary" : "Salary",
        "u_phone" : "Phone",
        "u_cname" : "Country",
        }

class CreatePatient(forms.ModelForm):
    class Meta:
        model = models.Patients
        fields = "__all__"





class ErasePatient(forms.CharField):
    class Meta:
        model = models.Patients
        fields = ['u_email']

class UpdatePatient(forms.ModelForm):
    class Meta:
        model = models.Patients
        fields = "__all__"

        label = {
        "u_email" : "Email",
        "u_name" : "Name",
        "u_surname" : "Surname",
        "u_salary" : "Salary",
        "u_phone" : "Phone",
        "u_cname" : "Country",
        }


class CreateDisease(forms.ModelForm):
    class Meta:
        model = models.Disease
        fields = "__all__"





class EraseDisease(forms.CharField):
    class Meta:
        model = models.Disease
        fields = ['u_email']

class UpdateDisease(forms.ModelForm):
    class Meta:
        model = models.Disease
        fields = "__all__"

        label = {
        "u_email" : "Email",
        "u_name" : "Name",
        "u_surname" : "Surname",
        "u_salary" : "Salary",
        "u_phone" : "Phone",
        "u_cname" : "Country",
        }

class CreateDiscover(forms.ModelForm):
    class Meta:
        model = models.Discover
        fields = "__all__"





class EraseDiscover(forms.CharField):
    class Meta:
        model = models.Discover
        fields = ['u_email']

class UpdateDiscover(forms.ModelForm):
    class Meta:
        model = models.Discover
        fields = "__all__"

        label = {
        "u_email" : "Email",
        "u_name" : "Name",
        "u_surname" : "Surname",
        "u_salary" : "Salary",
        "u_phone" : "Phone",
        "u_cname" : "Country",
        }

class CreatePD(forms.ModelForm):
    class Meta:
        model = models.PatientDisease
        fields = "__all__"





class ErasePD(forms.CharField):
    class Meta:
        model = models.PatientDisease
        fields = ['u_email']

class UpdatePD(forms.ModelForm):
    class Meta:
        model = models.PatientDisease
        fields = "__all__"

        label = {
        "u_email" : "Email",
        "u_name" : "Name",
        "u_surname" : "Surname",
        "u_salary" : "Salary",
        "u_phone" : "Phone",
        "u_cname" : "Country",
        }


class CreatePS(forms.ModelForm):
    class Meta:
        model = models.PublicServant
        fields = "__all__"





class ErasePS(forms.CharField):
    class Meta:
        model = models.PublicServant
        fields = ['u_email']

class UpdatePS(forms.ModelForm):
    class Meta:
        model = models.PublicServant
        fields = "__all__"

        label = {
        "u_email" : "Email",
        "u_name" : "Name",
        "u_surname" : "Surname",
        "u_salary" : "Salary",
        "u_phone" : "Phone",
        "u_cname" : "Country",
        }


class CreateDoctor(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = "__all__"





class EraseDoctor(forms.CharField):
    class Meta:
        model = models.Doctor
        fields = ['u_email']

class UpdateDoctor(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = "__all__"

        label = {
        "u_email" : "Email",
        "u_name" : "Name",
        "u_surname" : "Surname",
        "u_salary" : "Salary",
        "u_phone" : "Phone",
        "u_cname" : "Country",
        }


class CreateSpecialize(forms.ModelForm):
    class Meta:
        model = models.Specialize
        fields = "__all__"





class EraseSpecialize(forms.CharField):
    class Meta:
        model = models.Specialize
        fields = ['u_email']

class UpdateSpecialize(forms.ModelForm):
    class Meta:
        model = models.Specialize
        fields = "__all__"

        label = {
        "u_email" : "Email",
        "u_name" : "Name",
        "u_surname" : "Surname",
        "u_salary" : "Salary",
        "u_phone" : "Phone",
        "u_cname" : "Country",
        }


class CreateRecord(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = '__all__'

class EraseRecord(forms.CharField):
    class Meta:
        model = models.Record
        fields = ['u_email']

class UpdateRecord(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = '__all__'