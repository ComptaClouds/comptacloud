from django.shortcuts import render
from .forms import CreationForm
from django.shortcuts import redirect,get_object_or_404
from .models import*
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



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