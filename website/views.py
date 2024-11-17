from django.shortcuts import render, HttpResponse
from .models import Users
from sqlalchemy import URL, create_engine, text
from tabulate import tabulate

DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASS = "1488"
DB_NAME = "ASS3"


def tuptolist(res):
    out = list()
    for t in res:
        out.append(list(t))
    return out


def doctor_list(request):# once in templates directory
    doctors = Users.objects.raw("select u_name as nome, u_surname as cognome, dc_degree as degree, u_phone as phone, u_email from users join doctor on dc_email like u_email order by u_salary limit 5;")         #user_list
    return render(request, 'Users/doctors.html', {'doctors' : doctors})

