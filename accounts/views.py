from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.contrib import messages
from datetime import datetime
from django.utils import timezone


def signup(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('post:index')
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.created_date = timezone.now()
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Hesab aktivləşdirilməsi'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            to_list = [to_email]
            from_mail = settings.EMAIL_HOST_USER
            send_mail(mail_subject, message, from_mail, to_list)
            messages.success(request,
                             'Təbriklər,uğurla qeydiyyatdan keçdiniz!Xahiş edirik mailinizə gələn mesajı təsdiq edəsiniz!')
            return HttpResponseRedirect('/login/')
    else:
        form = SignupForm()
    context['form'] = form
    return render(request, 'accounts/signup.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.<a href="/login">Daxil ol</a>')
    else:
        return HttpResponse('Activation link is invalid!')

def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('post:index')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('post:index')
    context['form'] = form
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('post:index')