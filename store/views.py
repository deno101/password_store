from django.shortcuts import render, redirect
from store.decorators import validate_method
from store.forms import LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, password=form.data.get('password'), username=form.data.get('username'))

            if user is not None:
                login(request, user)
                redirect('login')
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})

    elif request.method == "GET":
        return render(request, 'login.html')
