from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, ChangePasswordForm
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:index')
    else:
        register_form = SignupForm()
    return render(request, 'registration/signup.html')


@login_required(login_url='/login/')
def change_password(request):
    massage = ''
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('main:dashbord')
    else:
        massage = 'Erroe When Change Password'
    context = {'massage': massage}
    return render(request, 'userapp/password_change.html', context)
