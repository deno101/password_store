from django.shortcuts import render, redirect
from store.decorators import validate_method
from django.contrib.auth.decorators import login_required
from store.forms import LoginForm, AddForm
from django.contrib.auth import authenticate, login
from store.models import PasswordStore
from django.http import HttpResponseBadRequest


# Create your views here.
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, password=form.data.get('password'), username=form.data.get('username'))

            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})

    elif request.method == "GET":
        return render(request, 'login.html')
    else:
        return HttpResponseBadRequest()


@validate_method('GET')
@login_required(login_url="/core_pssd/login/")
def home(requests):
    domains = PasswordStore.objects.all()
    domains_clean = set()
    for x in domains:
        domains_clean.add(x.site)
    return render(requests, 'home.html', {
        'domains': domains_clean,
    })


@login_required(login_url='/core_pssd/login')
@validate_method('GET')
def show_password(request, site):
    data = PasswordStore.objects.filter(site=site)
    if len(data) == 0:
        return redirect('home')

    return render(request, 'password_view.html', {
        'data': data,
        'title': site
    })


@login_required(login_url='/core_pssd/login')
def add_credentials(request):
    if request.method == 'POST':
        form = AddForm(request.POST)

        if form.is_valid():
            PasswordStore.objects.create(
                site=form.data.get('site'),
                username=form.data.get('username'),
                password=form.data.get('password')
            )

            return redirect('home')
    elif request.method == 'GET':
        return render(request, 'add.html')
    else:
        return HttpResponseBadRequest()


# @login_required(login_url='/core_pssd/login')
def edit_credentials(requests, id):
    return render(requests, 'edit.html')
