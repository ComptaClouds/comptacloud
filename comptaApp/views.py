from django.shortcuts import render
from .forms import CreationForm
import json
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
import json
from django.http.response import JsonResponse


# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from django.db.models import Q


from .forms import*







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
    ab={}

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,request.FILES, instance=request.user)

        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            ab['a']=12
           # return redirect('home')
            return HttpResponse(json.dumps(ab),content_type="application/json")


    else:
            form = CustomUserChangeForm(instance=request.user)
            args={'form':form}
            return render(request, 'modifier.html',args)


def liaisons(request):
    if request.method == 'POST':
        form = liaison(request.POST)
        if form.is_valid():
            for s in form.cleaned_data["relations"]:
                a=request.POST["comptableid"]
                b=CustomUser.objects.get(id=a)
                b.relations.add(s)
        return HttpResponse(a)
    else:
            form = liaison()
            args={'form':form}
            return render(request, 'liaisons.html',args)


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


def saisiesoperations(request):
    if request.method == "POST":
        operation = request.POST['libelle']
        entrepris = request.POST['entrep']
        entrepri = CustomUser.objects.get(username=entrepris)
        fournisseu = request.POST['movies']
        if CustomUser.objects.filter(groups=3,username=fournisseu).exists() == False:
                CustomUser.objects.create(username=fournisseu)
                user=CustomUser.objects.get(username=fournisseu)
                grouper=Group.objects.get(id=3)
                user.groups.add(grouper)
        fournisse = CustomUser.objects.get(username=fournisseu)
        operationcompta.objects.create(libelle=operation,typejournal_idtypejournal=1,entrepriseid_id=entrepri.id,fournisseurs_id=fournisse.id)
        return HttpResponse('')
    else:
        ent=CustomUser.objects.filter(groups=2)
        four = CustomUser.objects.filter(groups=3)
        return render(request, 'saisies_operations.html',{'ent':ent,'four':four})

def imputation(request):
    if request.method == "POST":
        op=request.POST['idoperation']
        userimpute=request.POST['useridimputer']
        post=request.POST['champs']
        post2 = request.POST['champs2']
        comptes=request.POST['comptes']
        comptes2 = request.POST['comptes2']
        q = QueryDict(post, mutable=True)
        q2 = QueryDict(post2, mutable=True)
        q3 = QueryDict(comptes, mutable=True)
        q4 = QueryDict(comptes2, mutable=True)
        ukeys=q.pop('champs')
        ukeys2 = q2.pop('champs2')
        ukeys3 = q3.pop('comptes')
        ukeys4 = q3.pop('comptes2')
        cpt=0
        cpt2=0
        for nbr in ukeys:
            co=ukeys3[cpt]
            comptid=co.split("-")
            dbiter=Debit.objects.create(montant=nbr,compte_compteid=comptid[0])
            cpt=cpt+1
            dbiter.save()

        for nbr in ukeys2:
            co2 = ukeys4[cpt2]
            comptid2 = co2.split("-")
            cditer=Credit.objects.create(montant=nbr,compte_compteid=comptid2[0])
            cpt2 = cpt2 + 1
            cditer.save()

        ope=operationcompta.objects.get(id=op)
        ope.useridimputer=userimpute
        ope.save()
        return HttpResponse('')
    else:
        for f in operationcompta.objects.filter(useridimputer__isnull=True)[:1]:
            opere=f.libelle
            operationconcernee=f.id
        h=operationcompta.objects.all()
        count=operationcompta.objects.all().count()
        j=operationcompta.objects.filter(useridimputer__isnull=True)
        countfiltre=operationcompta.objects.filter(useridimputer__isnull=True).count()

        return render(request, 'imputation.html',{'opere':opere,'operationconcernee':operationconcernee,'h':h,'j':j,'count':count,'countfiltre':countfiltre})


def fourni(request):
    if request.method == "POST":
        return HttpResponse('debitcredit')
    else:
        return render(request, 'saisiesoperations.html')


def afficherfournisseurs(request):
    ab = {}
    if request.method == 'POST':
            variable=request.POST['fournir']
            variable2=CustomUser.objects.get(username=variable)
            variable3=list(operationcompta.objects.filter(entrepriseid_id=variable2.id).values('fournisseurs_id'))
            a=[]
            for i in variable3:
                a.append(i['fournisseurs_id'])
            tableau=[]
            for e in a:
                f=CustomUser.objects.get(id=e)
                tableau.append(f.username)
            g=list(tableau)

            ab['a'] = g
            # return redirect('home')
            return HttpResponse(json.dumps(ab), content_type="application/json")
