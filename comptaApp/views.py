from django.shortcuts import render
from .forms import CreationForm
from django.shortcuts import redirect,get_object_or_404
from .models import*
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.utils.encoding import force_text
import pprint


# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from django.db.models import Q

from .models import CustomUser
from .forms import CustomUserCreationForm,continuerenregistrement,CustomUser,CustomUserChangeForm,DocumentForm,SignUpForm,autorisation







#...

from django.contrib import auth
from django.contrib.auth.decorators import permission_required
#...


def autorise(request):
    if request.method == 'POST':
        form = autorisation(request.POST)
        if form.is_valid():
            for a in form.cleaned_data["utilise"]:
                a.autorise=True
                a.save()
            return redirect('autorise')
    else:
        form = autorisation()
    return render(request, 'autorisation.html', {
        'form': form,

    })


def modifier(request):


    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,request.FILES, instance=request.user)

        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            return redirect('home')


    else:
            form = CustomUserChangeForm(instance=request.user)
            args={'form':form}
            return render(request, 'modifier.html',args)


def enregistrement(request):
    if request.method == 'POST':
        form = continuerenregistrement(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            user=form.save(commit=False)
            if user.valide is False:
                user.valide=True
            user.save()
            return redirect('home')
    else:
            form = continuerenregistrement(instance=request.user)
            args={'form':form}
            return render(request, 'enregistrement.html',args)




def login(request):
    if request.user.is_authenticated:
        return redirect('admin_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')
    return render(request, 'registration/home.html')


def logout(request):
    auth.logout(request)
    return render(request,'registration/home.html')


def admin_page(request):
    if not request.user.is_authenticated:
        return redirect('blog_login')



    a=request.user.username
    b = request.user.email
    c= request.user.groups.all()[0]
    p=c.permissions.all
    return render(request, 'blog2/admin_page.html',{'a':a,'b':b, 'd':p})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            a=document.entreprise
            if Document.objects.filter(entreprise=a).count()==3:
              return render(request, 'maximumatteint.html')
            document.save()

            return redirect('model_form_upload')
    else:
        form = DocumentForm(instance=request.user)
    return render(request, 'model_form_upload.html', {
        'form': form,

    })


def SignUp(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user.groups.add(form.cleaned_data["group"])
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        auth.login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')





def creeruser(request):
    if request.method == "POST":
        form = CreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('voiruser', pk=user.pk)
    else:
        form = CreationForm()
        return render(request, 'blog/creeruser_edit.html', {'form': form})



def voiruser(request, pk):
    posts = get_object_or_404(User2 , pk=pk)
    return render(request, 'blog/voiruser_edit.html', {'posts': posts})

def voiruser2(request):
    posts = User2.objects.all()
    return render(request, 'blog/voiruser_edit2.html', {'posts': posts})



def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('login.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')

def main(request):
    return render(request, 'blog/login.html', {})