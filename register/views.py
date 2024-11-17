from django.shortcuts import render, redirect, reverse, get_object_or_404
from . import forms
from . import models
from .forms import UpdateUser
from django.apps import apps


def list_user(request, Model):
    mdl = apps.get_model('register', Model)
    usrs = mdl.objects.all()
        #objs = models.Users.objects.all()

    return render(request, f'Register/list_Users.html', {'objs' : usrs, 'Model':Model})

def new_user(request, Model):
    if request.method == 'POST':
        form = forms.CreateUser(request.POST, Model)
        if form.is_valid():
            newuser = form.save(commit = False)
            newuser.save()
            return redirect(request.get_full_path().split('new')[0] + 'list/' + Model)
    else:
        form = forms.CreateUser()
    return render(request, 'Register/register.html', { 'form' : form, 'Model':Model})

def erase_user(request, Model, k1):
    mdl = apps.get_model('register', Model)
    obj = get_object_or_404(mdl, pk = k1)

    if request.method == 'POST':
        obj.delete()
        return redirect(request.get_full_path().split('erase')[0] + 'list/' + Model)

    return render(request, 'Register/erase.html', { 'obj' : obj, 'k1':k1, 'Model':Model})

def update_user(request, Model, k1):
    mdl = apps.get_model('register', Model)
    obj = get_object_or_404(mdl, pk = k1)

    form = UpdateUser(instance=obj)
    if request.method == 'POST':
        form = forms.UpdateUser(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(request.get_full_path().split('update')[0] + 'list/' + Model)
    template_name = "Register/update.html"
    context = {"form": form, 'k1':k1, 'Model':Model}
    return render(request, template_name, context)

def show_one(request, Model, k1):
    mdl = apps.get_model('register', Model)
    obj = get_object_or_404(mdl, pk = k1)

    k = []
    for f in mdl._meta.get_fields():
        k.append((f.name, f))
    keys = []
    for i in k:
        if i[0].__contains__('_'):
            keys.append(i[0])
    fields = [getattr(obj, f) for f in keys]
    verbn = [k.split('_')[1].capitalize() for k in keys]

    template_name = "Register/show_one.html"
    context = { 'k1': k1, 'Model': Model, 'verbn' : verbn, 'obj' : fields}
    return render(request, template_name, context)