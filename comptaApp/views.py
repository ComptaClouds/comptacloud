
from django.shortcuts import redirect,get_object_or_404
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
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
import json
from django.db.models import Avg, Max, Min, Sum
import datetime
from .forms import*
from django.contrib import auth
from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils



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
        doc = Document.objects.all()
        return render(request, 'saisies_operations.html',{'ent':ent,'four':four,'doc':doc})

def imputationss(request):
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
        ukeys4 = q4.pop('comptes2')
        cpt=0
        cpt2=0

        ope = operationcompta.objects.get(id=op)
        ope.useridtranscription = userimpute
        ope.save()

        imputa=imputation.objects.create(misajour=1, operation_id=op, user_id=userimpute)
        imputa.save()
        imput=imputation.objects.get(misajour=1, operation_id=op)
        imputid=imput.imputationid

        for nbr in ukeys:
            co=ukeys3[cpt]
            print(co)
            comptid=co.split("-")
            dbiter=Debit.objects.create(montant=nbr,compte_compteid=comptid[0],libellecompte=comptid[1],imputation_id=imputid)
            cpt=cpt+1
            dbiter.save()

        for nbr in ukeys2:
            co2 = ukeys4[cpt2]
            comptid2 = co2.split("-")
            cditer=Credit.objects.create(montant=nbr,compte_compteid=comptid2[0],libellecompte=comptid2[1],imputation_id=imputid)
            cpt2 = cpt2 + 1
            cditer.save()


        return HttpResponse('')
    else:
        for f in operationcompta.objects.filter(useridtranscription__isnull=True)[:1]:
            opere=f.libelle
            operationconcernee=f.id
        h=operationcompta.objects.all()
        count=operationcompta.objects.all().count()
        j=operationcompta.objects.filter(useridtranscription__isnull=True)
        countfiltre=operationcompta.objects.filter(useridtranscription__isnull=True).count()


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

def scan(request):

    # construct the argument parser and parse the arguments
    args = {'image': 'images/page.jpg'}
    print(args)
    # load the image and compute the ratio of the old height
    # to the new height, clone it, and resize it
    image = cv2.imread(args["image"])

    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height=500)

    # convert the image to grayscale, blur it, and find edges
    # in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)

    # show the original image and the edge detected image
    print("STEP 1: Edge Detection")
    cv2.imshow("Image", image)
    cv2.imshow("Edged", edged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # find the contours in the edged image, keeping only the
    # largest ones, and initialize the screen contour
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break

    # show the contour (outline) of the piece of paper
    print("STEP 2: Find contours of paper")
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("Outline", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # apply the four point transform to obtain a top-down
    # view of the original image
    warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

    # convert the warped image to grayscale, then threshold it
    # to give it that 'black and white' paper effect
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    T = threshold_local(warped, 11, offset=10, method="gaussian")
    warped = (warped > T).astype("uint8") * 255

    # show the original and scanned images
    print("STEP 3: Apply perspective transform")
    cv2.imshow("Original", imutils.resize(orig, height=650))
    cv2.imshow("Scanned", imutils.resize(warped, height=650))
    print(Scanned)
    cv2.waitKey(0)



def modifierimputation(request,pk):
    if request.method == 'POST':
        op = request.POST['idoperation']
        userimpute = request.POST['useridimputer']
        post = request.POST['champs']
        post2 = request.POST['champs2']
        comptes = request.POST['comptes']
        comptes2 = request.POST['comptes2']
        q = QueryDict(post, mutable=True)
        q2 = QueryDict(post2, mutable=True)
        q3 = QueryDict(comptes, mutable=True)
        q4 = QueryDict(comptes2, mutable=True)
        ukeys = q.pop('champs')
        ukeys2 = q2.pop('champs2')
        ukeys3 = q3.pop('comptes')
        ukeys4 = q4.pop('comptes2')
        cpt = 0
        cpt2 = 0

        impu = imputation.objects.get(misajour=1, operation_id=op)
        impu.misajour=0
        impu.save()
        imputa = imputation.objects.create(misajour=1, operation_id=op, user_id=userimpute)
        imputa.save()
        imput = imputation.objects.get(misajour=1, operation_id=op)
        imputid = imput.imputationid

        for nbr in ukeys:
            if(nbr!=''):
                if(ukeys3[cpt]!=''):
                    co = ukeys3[cpt]
                print(co)
                comptid = co.split("-")
                dbiter = Debit.objects.create(montant=nbr, compte_compteid=comptid[0], libellecompte=comptid[1],
                                          imputation_id=imputid)
                cpt = cpt + 1
                dbiter.save()

        for nbr in ukeys2:
            if (nbr != ''):
                if (ukeys4[cpt] != ''):
                    co2 = ukeys4[cpt2]
                comptid2 = co2.split("-")
                cditer = Credit.objects.create(montant=nbr, compte_compteid=comptid2[0], libellecompte=comptid2[1],
                                           imputation_id=imputid)
                cpt2 = cpt2 + 1
                cditer.save()

        return HttpResponse('')

    else:
        post = get_object_or_404(imputation, pk=pk)
        imputationnner=post.imputationid
        operationid = post.operation_id
        operationget = operationcompta.objects.get(id=operationid)
        operationname = operationget.libelle
        debit = Debit.objects.filter(imputation_id=post.imputationid)
        credit = Credit.objects.filter(imputation_id=post.imputationid)
        return render(request, 'modifierimputation.html',{'post': post ,'debit': debit, 'credit': credit,'operation':operationid,'imputationid':imputationnner,'operationname':operationname})


def listeoperationsimputees(request):
        debit=Debit.objects.all()
        credit=Credit.objects.all()
        operation=operationcompta.objects.all()
        imputations=imputation.objects.filter(misajour=1)
        return render(request, 'listeoperationsimputees.html',{'debit':debit,'credit':credit,'operation':operation,'imputations':imputations})


def journal_central(request):
    ag = {}
    if request.method == 'POST':
        datedebut=request.POST['datedebut']
        datefin=request.POST['datefin']
        typejournal=request.POST['typejournal']
        print(typejournal)

        if(datedebut=='' or datefin==''):
            maxdate=imputation.objects.filter(misajour=1).aggregate(Max('date'))
            fin=maxdate['date__max'].date()

            mindate=imputation.objects.filter(misajour=1).aggregate(Min('date'))
            debut = mindate['date__min'].date()

        else:

            #decoupe les dates a partir des tirets -
            datedebut = datedebut.split('-')
            datefin = datefin.split('-')

            #les dates sont de type string il faut les mettre de type int pour pouvoir utiliser datetime
            annee = datedebut[0]
            annee = int(annee)
            mois = datedebut[1]
            mois = int(mois)
            jour = datedebut[2]
            jour = int(jour)

            annee2 = datefin[0]
            annee2 = int(annee2)
            mois2 = datefin[1]
            mois2 = int(mois2)
            jour2 = datefin[2]
            jour2 = int(jour2)
            print(mois)

            #rendre les dates au format date de python
            debut = datetime.date(annee, mois, jour)
            fin = datetime.date(annee2, mois2, jour2)



        date = imputation.objects.filter(misajour=1)

        idimputation = []
        datedebit = []
        datecredit = []
        numcomptedebit = []
        montantdebit = []
        libellecomptedebit = []
        numcomptecredit = []
        montantcredit = []
        libellecomptecredit = []
        idimputationdebit = []
        idimputationcredit = []

        a=[]
        tab=[]
        t=[]


        for dates in date:
            if(typejournal!='tous' and typejournal!='grandlivre' and typejournal!='balance'):
                c=operationcompta.objects.get(id=dates.operation_id)
                if(c.typejournal_idtypejournal==int(typejournal)):
                    a.append(dates.imputationid)
            else:
                a.append(dates.imputationid)

        print(debut)
        for a in a:

            s=imputation.objects.get(imputationid=a)
            if(s.date.date()>=debut and s.date.date()<=fin):
                #mets les dates dans le tableau a
                idimputation.append(s.imputationid)

        for id in idimputation:
            s=imputation.objects.get(imputationid=id)

            numcompte=Debit.objects.filter(imputation_id=s.imputationid)
            numcompte2 = Credit.objects.filter(imputation_id=s.imputationid)

            if (typejournal == 'grandlivre' or typejournal == 'balance'):
                tab.extend(list(numcompte.values('compte_compteid')))
                tab.extend(list(numcompte2.values('compte_compteid')))

            for numcompte in numcompte:
                    datedebit.append(str(s.date.date()))
                    numcomptedebit.append(numcompte.compte_compteid)
                    montantdebit.append(numcompte.montant)
                    libellecomptedebit.append(numcompte.libellecompte)
                    idimputationdebit.append(numcompte.imputation_id)


            for numcompte2 in numcompte2:
                    datecredit.append(str(s.date.date()))
                    numcomptecredit.append(numcompte2.compte_compteid)
                    montantcredit.append(numcompte2.montant)
                    libellecomptecredit.append(numcompte2.libellecompte)
                    idimputationcredit.append(numcompte.imputation_id)

        y=[]
        if(typejournal=='grandlivre' or typejournal=='balance'):
            for tab in tab:
                t.append(tab['compte_compteid'])
            idimputation=t[:]

            print(idimputation)
            print(t)
            for t in t:

                if (idimputation.count(t) > 1):
                    print(t)
                    idimputation.remove(t)

            y=idimputation[:]
            if(typejournal=='balance'):
                for y in y:
                    y=str(y)
                    if(int(y[0])%9==0):
                        y=int(y)
                        idimputation.remove(y)

            idimputationdebit=numcomptedebit
            idimputationcredit=numcomptecredit

        print(idimputation)

        #tableau qu'on va appeler en mode json dans le javascripts par la valeur de retour data
        ag['idimputation'] = idimputation
        ag['idimputationdebit'] = idimputationdebit
        ag['idimputationcredit'] = idimputationcredit
        ag['datedebit'] = datedebit
        ag['datecredit'] = datecredit
        ag['numcomptedebit'] = numcomptedebit
        ag['numcomptecredit'] = numcomptecredit
        ag['montantdebit'] = montantdebit
        ag['montantcredit'] = montantcredit
        ag['libellecomptedebit'] = libellecomptedebit
        ag['libellecomptecredit'] = libellecomptecredit
        ag['typejournal'] = typejournal


        return HttpResponse(json.dumps(ag), content_type="application/json")

    else:
        debit = Debit.objects.all()
        credit = Credit.objects.all()
        operation = operationcompta.objects.all()
        imputations = imputation.objects.filter(misajour=1)
        typejournal = Typejournal.objects.all()
        return render(request, 'journalcentral.html',
                      {'debit': debit, 'credit': credit, 'operation': operation, 'imputations': imputations,'typejournal':typejournal})