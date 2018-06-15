


class fournisseurs(models.Model):
    nom = models.CharField(max_length=45, blank=True, null=True)




class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.entreprise, filename)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documents',on_delete=models.CASCADE,default=1)
    entreprise =  models.CharField(max_length=255, default='merde')



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    capital = models.IntegerField()
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Compte(models.Model):
    compteid = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45, blank=True, null=True)
    classe = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compte'


class Credit(models.Model):
    idcredit = models.AutoField(primary_key=True)
    operation_operationid = models.IntegerField()
    compte_compteid = models.IntegerField()
    operation_user_2_useridsaisie = models.IntegerField()
    operation_user_2_useridimputer = models.IntegerField()
    operation_typejournal_idtypejournal = models.PositiveIntegerField()
    double_2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit'
        unique_together = (('idcredit', 'operation_operationid', 'compte_compteid', 'operation_user_2_useridsaisie', 'operation_user_2_useridimputer', 'operation_typejournal_idtypejournal'),)


class Debit(models.Model):
    iddebit = models.AutoField(primary_key=True)
    operation_operationid = models.IntegerField()
    compte_compteid = models.IntegerField()
    operation_user_2_useridsaisie = models.IntegerField()
    operation_user_2_useridimputer = models.IntegerField()
    operation_typejournal_idtypejournal = models.PositiveIntegerField()
    montant = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debit'
        unique_together = (('iddebit', 'operation_operationid', 'compte_compteid', 'operation_user_2_useridsaisie', 'operation_user_2_useridimputer', 'operation_typejournal_idtypejournal'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'




class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Typejournal(models.Model):
    idtypejournal = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typejournal'


class User2(models.Model):
    userid = models.AutoField(primary_key=True)
    denomination = models.CharField(max_length=45, blank=True, null=True)
    siege = models.CharField(max_length=45, blank=True, null=True)
    objet = models.CharField(max_length=45, blank=True, null=True)
    capital = models.FloatField(blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False


        db_table = 'user_2'

        class DocumentForm(forms.ModelForm):
            entreprise = forms.ModelChoiceField(queryset=CustomUser.objects.filter(groups=1),
                                                required=True)

            class Meta:
                model = Document
                fields = ('description', 'document', 'entreprise',)

        class liaison(forms.ModelForm):
            relations = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.filter(groups=1),
                                                       widget=forms.CheckboxSelectMultiple)

            class Meta:
                model = CustomUser
                fields = ('relations',)


def saisiesoperations(request):
    if request.method == "POST":
        username = request.POST['nom']
        operation = request.POST['libelle']
        type = request.POST['type']
        if Fournisseurs.objects.filter(nom=username).exists() == False:
                Fournisseurs.objects.create(nom=username)
        operationcompta.objects.create(libelle=operation,typejournal_idtypejournal=1)
        return HttpResponse('')
    else:
        return render(request, 'saisies_operations.html')

< !DOCTYPE
html >
< html >
< body >

< p > Write
something in the
text
field
to
trigger
a
function. < / p >

< input
type = "text"
id = "1"
oninput = "myFunction()" >
< input
type = "text"
id = "3"
oninput = "myFunction()" >
< input
type = "submit"
disabled = 'disabled'
id = 'r' >

< p
id = "demo" > < / p >

< script >
function
myFunction()
{
    var
x = 0;
for (var i = 1; i <= 3; i++)
{
if (document.getElementById(i) == null)
{i + +;}
var
p = parseInt(document.getElementById(i).value);
if (document.getElementById(i).value == '')
{p = 0;}
var
x = x + p;
if (x == 3)
{document.getElementById("r").setAttribute("enabled", "enabled");
document.getElementById("r").removeAttribute("disabled");}
else {document.getElementById("r").setAttribute("disabled", "disabled");
document.getElementById("r").removeAttribute("enabled");}

}
document.getElementById("demo").innerHTML = "You wrote: " + x;

}
< / script >

< / body >
< / html >

a


<script>
    function addid(element){

        for(i=1;i<=2;i++){document.getElementById(i).removeAttribute("class"); }
        element.setAttribute("class","comptes")
    }

</script>


var options = {
	url: "{% static 'js/plan.json' %}",
	listLocation: "SYSCOA",

	getValue: function(element) {
	$a=element.classe+" - "+element.libelle;
	if(element.classe>=10){$a="&nbsp&nbsp"+element.classe+" - "+element.libelle;}
	return $a;
},



/*RECUPERER LES DATAS DUN JSON*/

down vote
accepted
This will do it:

var json = (function () {
    var json = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': my_url,
        'dataType': "json",
        'success': function (data) {
            json = data;
        }
    });
    return json;
})(); /*/*/*/




















if(request.term.charAt(0).match(/[0-9]/))
    var result=liste1 ;
else
    var result=liste2 ;
    response(result);

function({
                    term: request.term
                    },


                        function (data) {
                        response(data);
                    });












	list: {
	    maxNumberOfElements: 6,
		match: {
			enabled: true
		},
		onClickEvent: function() {
			var value = $(".comptes").getSelectedItemData().libelle;
			$(".comptes").val(value).trigger("change");

		},
		onHideListEvent: function() {
			$(".easy-autocomplete-container").children().attr("style","display:none");
			$(".comptes").attr("autofocus","autofocus");

		}

	}

};
console.log(options);
$(".comptes").easyAutocomplete(options);




















var json = [
        {
            libelle: "1",
            libelle1: "Comptes de ressources durables",
            value: "1 - Comptes de ressources durables"
        },
        {
            libelle: "10",
            libelle1: "Capital",
            value: "10 - Capital"
        },
        {
            libelle: "101",
            libelle1: "Capital social",
            value: "101 - Capital social"
        },
        {
            libelle: "102",
            libelle1: "Capital par dotation",
            value: "102 - Capital par dotation"
        },
        {
            libelle: "103",
            libelle1: "Capital personnel",
            value: "103 - Capital personnel"
        },
        {
            libelle: "104",
            libelle1: "Compte de l'exploitant",
            value: "104 - Compte de l'exploitant"
        },
        {
            libelle: "105",
            libelle1: "Primes liées Capitaux propres",
            value: "105 - Primes liées Capitaux propres"
        },
        {
            libelle: "106",
            libelle1: "Écarts de réévaluation",
            value: "106 - Écarts de réévaluation"
        },
        {
            libelle: "1061",
            libelle1: "Écarts de réévaluation légale",
            value: "1061 - Écarts de réévaluation légale"
        },
        {
            libelle: "1062",
            libelle1: "Écarts de réévaluation libre",
            value: "1062 - Écarts de réévaluation libre"
        },
        {
            libelle: "109",
            libelle1: "Actionnaires, capital souscrit, non appelé",
            value: "109 - Actionnaires, capital souscrit, non appelé"
        },
        {
            libelle: "11",
            libelle1: "Réserves",
            value: "11 - Réserves"
        },
        {
            libelle: "111",
            libelle1: "Réserve légale",
            value: "111 - Réserve légale"
        },
        {
            libelle: "113",
            libelle1: "Réserves réglementées",
            value: "113 - Réserves réglementées"
        },
        {
            libelle: "118",
            libelle1: "Autres réserves",
            value: "118 - Autres réserves"
        },
        {
            libelle: "12",
            libelle1: "Report à nouveau",
            value: "12 - Report à nouveau"
        },
        {
            libelle: "121",
            libelle1: "Report à nouveau créditeur",
            value: "121 - Report à nouveau créditeur"
        },
        {
            libelle: "129",
            libelle1: "Report à nouveau débiteur",
            value: "129 - Report à nouveau débiteur"
        },
        {
            libelle: "14",
            libelle1: "Subventions d'investissement",
            value: "14 - Subventions d'investissement"
        },
        {
            libelle: "15",
            libelle1: "Provisions réglementées et assimilées",
            value: "15 - Provisions réglementées et assimilées"
        },
        {
            libelle: "151",
            libelle1: "Amortissements dérogatoires",
            value: "151 - Amortissements dérogatoires"
        },
        {
            libelle: "152",
            libelle1: "Plus-values cession à réinvestir",
            value: "152 - Plus-values cession à réinvestir"
        },
        {
            libelle: "153",
            libelle1: "Fonds réglementés",
            value: "153 - Fonds réglementés"
        },
        {
            libelle: "155",
            libelle1: "Provis. réglementées sur Immobilisations.",
            value: "155 - Provis. réglementées sur Immobilisations."
        },
        {
            libelle: "156",
            libelle1: "Provis. réglementées sur stocks",
            value: "156 - Provis. réglementées sur stocks"
        },
        {
            libelle: "16",
            libelle1: "Emprunts et dettes assimilées",
            value: "16 - Emprunts et dettes assimilées"
        },
        {
            libelle: "161",
            libelle1: "Emprunts obligataires",
            value: "161 - Emprunts obligataires"
        },
        {
            libelle: "1611",
            libelle1: "Emprunts obligataires ordinaires",
            value: "1611 - Emprunts obligataires ordinaires"
        },
        {
            libelle: "1612",
            libelle1: "Emprunts obligataires convertibles",
            value: "1612 - Emprunts obligataires convertibles"
        },
        {
            libelle: "1618",
            libelle1: "Emprunts obligataires",
            value: "1618 - Emprunts obligataires"
        },
        {
            libelle: "162",
            libelle1: "Emprunts Établissement crédit",
            value: "162 - Emprunts Établissement crédit"
        },
        {
            libelle: "163",
            libelle1: "Avances reçues de l'état",
            value: "163 - Avances reçues de l'état"
        },
        {
            libelle: "164",
            libelle1: "Avances reçues, C/C bloqués",
            value: "164 - Avances reçues, C/C bloqués"
        },
        {
            libelle: "165",
            libelle1: "Dépôts et cautionnements reçus",
            value: "165 - Dépôts et cautionnements reçus"
        },
        {
            libelle: "167",
            libelle1: "Avances à conditions. particulières",
            value: "167 - Avances à conditions. particulières"
        },
        {
            libelle: "168",
            libelle1: "Autres emprunts et dettes",
            value: "168 - Autres emprunts et dettes"
        },
        {
            libelle: "166",
            libelle1: "Intérêts courus",
            value: "166 - Intérêts courus"
        },
        {
            libelle: "1661",
            libelle1: "Sur emprunts obligataires",
            value: "1661 - Sur emprunts obligataires"
        },
        {
            libelle: "1662",
            libelle1: "Sur emprunts établissements de. crédit",
            value: "1662 - Sur emprunts établissements de. crédit"
        },
        {
            libelle: "1663",
            libelle1: "Sur avances reçues de l'état",
            value: "1663 - Sur avances reçues de l'état"
        },
        {
            libelle: "1664",
            libelle1: "Sur avances reçues, C/C bloqués",
            value: "1664 - Sur avances reçues, C/C bloqués"
        },
        {
            libelle: "1665",
            libelle1: "Sur dépôts, cautionnements",
            value: "1665 - Sur dépôts, cautionnements"
        },
        {
            libelle: "1667",
            libelle1: "sur avances à conditions. particulières.",
            value: "1667 - sur avances à conditions. particulières."
        },
        {
            libelle: "1668",
            libelle1: "Sur autres emprunts et dettes",
            value: "1668 - Sur autres emprunts et dettes"
        },
        {
            libelle: "17",
            libelle1: "Dettes crédit-bail et assimilé",
            value: "17 - Dettes crédit-bail et assimilé"
        },
        {
            libelle: "172",
            libelle1: "Emprunts crédit-bail immobilier",
            value: "172 - Emprunts crédit-bail immobilier"
        },
        {
            libelle: "173",
            libelle1: "Emprunts crédit-bail mobilier",
            value: "173 - Emprunts crédit-bail mobilier"
        },
        {
            libelle: "176",
            libelle1: "Intérêts courus",
            value: "176 - Intérêts courus"
        },
        {
            libelle: "1762",
            libelle1: "Sur emprunt. crédit-bail immobilier",
            value: "1762 - Sur emprunt. crédit-bail immobilier"
        },
        {
            libelle: "1763",
            libelle1: "Sur emprunt. crédit-bail mobilier",
            value: "1763 - Sur emprunt. crédit-bail mobilier"
        },
        {
            libelle: "1768",
            libelle1: "Sur emprunt. équivalent. autres. contrats",
            value: "1768 - Sur emprunt. équivalent. autres. contrats"
        },
        {
            libelle: "178",
            libelle1: "Emprunt. équivalents autres contrats",
            value: "178 - Emprunt. équivalents autres contrats"
        },
        {
            libelle: "18",
            libelle1: "Dettes liées",
            value: "18 - Dettes liées"
        },
        {
            libelle: "181",
            libelle1: "Dettes liées participations",
            value: "181 - Dettes liées participations"
        },
        {
            libelle: "182",
            libelle1: "Dettes liées sociétés en participation.",
            value: "182 - Dettes liées sociétés en participation."
        },
        {
            libelle: "183",
            libelle1: "Int. courus sur Dettes liées à des participations",
            value: "183 - Int. courus sur Dettes liées à des participations"
        },
        {
            libelle: "184",
            libelle1: "Comptes permanents bloqués",
            value: "184 - Comptes permanents bloqués"
        },
        {
            libelle: "185",
            libelle1: "Comptes permanents non bloqués",
            value: "185 - Comptes permanents non bloqués"
        },
        {
            libelle: "186",
            libelle1: "Comptes de liaison charges",
            value: "186 - Comptes de liaison charges"
        },
        {
            libelle: "187",
            libelle1: "Comptes de liaison produits",
            value: "187 - Comptes de liaison produits"
        },
        {
            libelle: "188",
            libelle1: "Comptes liaison : Sociétés en Part.",
            value: "188 - Comptes liaison : Sociétés en Part."
        },
        {
            libelle: "19",
            libelle1: "Provis.  Fin. Risques & Charges",
            value: "19 - Provis.  Fin. Risques & Charges"
        },
        {
            libelle: "2",
            libelle1: "Comptes d'actif immobilisé",
            value: "2 - Comptes d'actif immobilisé"
        },
        {
            libelle: "20",
            libelle1: "Charges immobilisées",
            value: "20 - Charges immobilisées"
        },
        {
            libelle: "201",
            libelle1: "Frais d'établissement",
            value: "201 - Frais d'établissement"
        },
        {
            libelle: "202",
            libelle1: "Charges à répartir",
            value: "202 - Charges à répartir"
        },
        {
            libelle: "206",
            libelle1: "Primes Remboursement Obligations",
            value: "206 - Primes Remboursement Obligations"
        },
        {
            libelle: "21",
            libelle1: "Immobilisations incorporelles",
            value: "21 - Immobilisations incorporelles"
        },
        {
            libelle: "211",
            libelle1: "Frais recherche et développement",
            value: "211 - Frais recherche et développement"
        },
        {
            libelle: "212",
            libelle1: "Brevets, licences, concessions",
            value: "212 - Brevets, licences, concessions"
        },
        {
            libelle: "213",
            libelle1: "Logiciels",
            value: "213 - Logiciels"
        },
        {
            libelle: "214",
            libelle1: "Marques",
            value: "214 - Marques"
        },
        {
            libelle: "215",
            libelle1: "Fonds commercial",
            value: "215 - Fonds commercial"
        },
        {
            libelle: "216",
            libelle1: "Droit au bail",
            value: "216 - Droit au bail"
        },
        {
            libelle: "217",
            libelle1: "Investissements de création",
            value: "217 - Investissements de création"
        },
        {
            libelle: "218",
            libelle1: "Autres droits, valeurs incorporelles.",
            value: "218 - Autres droits, valeurs incorporelles."
        },
        {
            libelle: "219",
            libelle1: "Immobilisations. incorporelles en cours",
            value: "219 - Immobilisations. incorporelles en cours"
        },
        {
            libelle: "2191",
            libelle1: "Frais recherche et développement",
            value: "2191 - Frais recherche et développement"
        },
        {
            libelle: "2193",
            libelle1: "Logiciels",
            value: "2193 - Logiciels"
        },
        {
            libelle: "2198",
            libelle1: "Autres droits, valeurs incorporelles.",
            value: "2198 - Autres droits, valeurs incorporelles."
        },
        {
            libelle: "22",
            libelle1: "Terrains",
            value: "22 - Terrains"
        },
        {
            libelle: "221",
            libelle1: "Terrains agricoles et forestiers",
            value: "221 - Terrains agricoles et forestiers"
        },
        {
            libelle: "222",
            libelle1: "Terrains nus",
            value: "222 - Terrains nus"
        },
        {
            libelle: "223",
            libelle1: "Terrains bâtis",
            value: "223 - Terrains bâtis"
        },
        {
            libelle: "224",
            libelle1: "Travaux mise en valeur terrains",
            value: "224 - Travaux mise en valeur terrains"
        },
        {
            libelle: "225",
            libelle1: "Terrains de gisement",
            value: "225 - Terrains de gisement"
        },
        {
            libelle: "226",
            libelle1: "Terrains aménagés",
            value: "226 - Terrains aménagés"
        },
        {
            libelle: "228",
            libelle1: "Autres terrains",
            value: "228 - Autres terrains"
        },
        {
            libelle: "229",
            libelle1: "Aménagements terrains en cours",
            value: "229 - Aménagements terrains en cours"
        },
        {
            libelle: "23",
            libelle1: "Bâtiments, installations. techniques",
            value: "23 - Bâtiments, installations. techniques"
        },
        {
            libelle: "231",
            libelle1: "Bâtiments sur sol propre",
            value: "231 - Bâtiments sur sol propre"
        },
        {
            libelle: "232",
            libelle1: "Bâtiments sur sol d'autrui",
            value: "232 - Bâtiments sur sol d'autrui"
        },
        {
            libelle: "233",
            libelle1: "Ouvrages d'infrastructure",
            value: "233 - Ouvrages d'infrastructure"
        },
        {
            libelle: "234",
            libelle1: "Installations techniques",
            value: "234 - Installations techniques"
        },
        {
            libelle: "235",
            libelle1: "Aménagement de bureaux",
            value: "235 - Aménagement de bureaux"
        },
        {
            libelle: "237",
            libelle1: "Bâtiments en concession",
            value: "237 - Bâtiments en concession"
        },
        {
            libelle: "238",
            libelle1: "Autres installations et agencements",
            value: "238 - Autres installations et agencements"
        },
        {
            libelle: "239",
            libelle1: "Bâtiment et installations en cours",
            value: "239 - Bâtiment et installations en cours"
        },
        {
            libelle: "2391",
            libelle1: "En cours sur Bâtiments sur sol propre",
            value: "2391 - En cours sur Bâtiments sur sol propre"
        },
        {
            libelle: "2392",
            libelle1: "En cours sur Bâtiments sur sol d'autrui",
            value: "2392 - En cours sur Bâtiments sur sol d'autrui"
        },
        {
            libelle: "2393",
            libelle1: "En cours sur Ouvrages d'infrastructure",
            value: "2393 - En cours sur Ouvrages d'infrastructure"
        },
        {
            libelle: "2394",
            libelle1: "En cours sur Installations techniques",
            value: "2394 - En cours sur Installations techniques"
        },
        {
            libelle: "2395",
            libelle1: "En cours sur Aménagement de bureaux",
            value: "2395 - En cours sur Aménagement de bureaux"
        },
        {
            libelle: "2397",
            libelle1: "En cours sur Bâtiments en concession",
            value: "2397 - En cours sur Bâtiments en concession"
        },
        {
            libelle: "2398",
            libelle1: "En cours sur Autres installations et agencements",
            value: "2398 - En cours sur Autres installations et agencements"
        },
        {
            libelle: "24",
            libelle1: "Matériel",
            value: "24 - Matériel"
        },
        {
            libelle: "241",
            libelle1: "Matériel, outillage industriel et commercial",
            value: "241 - Matériel, outillage industriel et commercial"
        },
        {
            libelle: "242",
            libelle1: "Matériel et outillage agricole",
            value: "242 - Matériel et outillage agricole"
        },
        {
            libelle: "243",
            libelle1: "Matériel Emballage récupérable",
            value: "243 - Matériel Emballage récupérable"
        },
        {
            libelle: "244",
            libelle1: "Matériel et mobilier",
            value: "244 - Matériel et mobilier"
        },
        {
            libelle: "245",
            libelle1: "Matériel de transport",
            value: "245 - Matériel de transport"
        },
        {
            libelle: "246",
            libelle1: "Immobilisations. animales, agricoles",
            value: "246 - Immobilisations. animales, agricoles"
        },
        {
            libelle: "248",
            libelle1: "Autres matériels",
            value: "248 - Autres matériels"
        },
        {
            libelle: "249",
            libelle1: "Matériel en cours",
            value: "249 - Matériel en cours"
        },
        {
            libelle: "2491",
            libelle1: "Matériel, outillage industriel et commercial en cours",
            value: "2491 - Matériel, outillage industriel et commercial en cours"
        },
        {
            libelle: "2492",
            libelle1: "Matériel et outillage agricole en cours",
            value: "2492 - Matériel et outillage agricole en cours"
        },
        {
            libelle: "2493",
            libelle1: "Matériel Emballage récupérable en cours",
            value: "2493 - Matériel Emballage récupérable en cours"
        },
        {
            libelle: "2494",
            libelle1: "Matériel et mobilier de bureau en cours",
            value: "2494 - Matériel et mobilier de bureau en cours"
        },
        {
            libelle: "2495",
            libelle1: "Matériel de transport en cours",
            value: "2495 - Matériel de transport en cours"
        },
        {
            libelle: "2496",
            libelle1: "Immobilisations. animales, agricoles en cours",
            value: "2496 - Immobilisations. animales, agricoles en cours"
        },
        {
            libelle: "2497",
            libelle1: "Agencements., aménagement. du matériel en cours",
            value: "2497 - Agencements., aménagement. du matériel en cours"
        },
        {
            libelle: "2498",
            libelle1: "Autres matériels en cours",
            value: "2498 - Autres matériels en cours"
        },
        {
            libelle: "25",
            libelle1: "Avances, acomptes versés sur immobilisations",
            value: "25 - Avances, acomptes versés sur immobilisations"
        },
        {
            libelle: "26",
            libelle1: "Titres de participation",
            value: "26 - Titres de participation"
        },
        {
            libelle: "27",
            libelle1: "Autres immobilisations. financières",
            value: "27 - Autres immobilisations. financières"
        },
        {
            libelle: "271",
            libelle1: "Prêts et créances non commerciales",
            value: "271 - Prêts et créances non commerciales"
        },
        {
            libelle: "272",
            libelle1: "Prêts au personnel",
            value: "272 - Prêts au personnel"
        },
        {
            libelle: "273",
            libelle1: "Créances sur l'Etat",
            value: "273 - Créances sur l'Etat"
        },
        {
            libelle: "274",
            libelle1: "Titres immobilisés",
            value: "274 - Titres immobilisés"
        },
        {
            libelle: "275",
            libelle1: "Dépôts et cautionnements versés",
            value: "275 - Dépôts et cautionnements versés"
        },
        {
            libelle: "276",
            libelle1: "Intérêts courus",
            value: "276 - Intérêts courus"
        },
        {
            libelle: "2761",
            libelle1: "Int. Courus Prêts et créances non commerciales",
            value: "2761 - Int. Courus Prêts et créances non commerciales"
        },
        {
            libelle: "2762",
            libelle1: "Int. Courus Prêts au personnel",
            value: "2762 - Int. Courus Prêts au personnel"
        },
        {
            libelle: "2763",
            libelle1: "Int. Courus Créances sur l'Etat",
            value: "2763 - Int. Courus Créances sur l'Etat"
        },
        {
            libelle: "2764",
            libelle1: "Int. Courus Titres immobilisés",
            value: "2764 - Int. Courus Titres immobilisés"
        },
        {
            libelle: "2765",
            libelle1: "Int. Courus Dépôts et cautionnements versés",
            value: "2765 - Int. Courus Dépôts et cautionnements versés"
        },
        {
            libelle: "2767",
            libelle1: "Int. Courus Créances rattachées à des participations",
            value: "2767 - Int. Courus Créances rattachées à des participations"
        },
        {
            libelle: "2768",
            libelle1: "Int. Courus Immobilisations financières diverses",
            value: "2768 - Int. Courus Immobilisations financières diverses"
        },
        {
            libelle: "277",
            libelle1: "Créances rattachées à des participations",
            value: "277 - Créances rattachées à des participations"
        },
        {
            libelle: "278",
            libelle1: "Immobilisations financières diverses",
            value: "278 - Immobilisations financières diverses"
        },
        {
            libelle: "28",
            libelle1: "Amortissements",
            value: "28 - Amortissements"
        },
        {
            libelle: "281",
            libelle1: "Amortis. : immobilisations. incorporelles",
            value: "281 - Amortis. : immobilisations. incorporelles"
        },
        {
            libelle: "2811",
            libelle1: "Amortissements. : frais R &D",
            value: "2811 - Amortissements. : frais R &D"
        },
        {
            libelle: "2812",
            libelle1: "Amortissements. : brevets, licences",
            value: "2812 - Amortissements. : brevets, licences"
        },
        {
            libelle: "2813",
            libelle1: "Amortissements des logiciels",
            value: "2813 - Amortissements des logiciels"
        },
        {
            libelle: "2814",
            libelle1: "Amortissements des marques",
            value: "2814 - Amortissements des marques"
        },
        {
            libelle: "2815",
            libelle1: "Amortissements. du fonds commercial",
            value: "2815 - Amortissements. du fonds commercial"
        },
        {
            libelle: "2816",
            libelle1: "Amortissements du droit au bail",
            value: "2816 - Amortissements du droit au bail"
        },
        {
            libelle: "2817",
            libelle1: "Amont. : investissements. création",
            value: "2817 - Amont. : investissements. création"
        },
        {
            libelle: "2818",
            libelle1: "Amortissements. autres  valeurs incorporelles.",
            value: "2818 - Amortissements. autres  valeurs incorporelles."
        },
        {
            libelle: "282",
            libelle1: "Amortissements des terrains",
            value: "282 - Amortissements des terrains"
        },
        {
            libelle: "283",
            libelle1: "Amortissements. : bâtiments, installations. ",
            value: "283 - Amortissements. : bâtiments, installations. "
        },
        {
            libelle: "2831",
            libelle1: "Amort. bâtim. industriels. sol propre",
            value: "2831 - Amort. bâtim. industriels. sol propre"
        },
        {
            libelle: "2832",
            libelle1: "Amort. bâtiments. industriels. sol autrui",
            value: "2832 - Amort. bâtiments. industriels. sol autrui"
        },
        {
            libelle: "2833",
            libelle1: "Amortissements. : ouvrages infrastructure",
            value: "2833 - Amortissements. : ouvrages infrastructure"
        },
        {
            libelle: "2834",
            libelle1: "Amont. : installations. techniques",
            value: "2834 - Amont. : installations. techniques"
        },
        {
            libelle: "2835",
            libelle1: "Amortissements. : aménagement. bureaux",
            value: "2835 - Amortissements. : aménagement. bureaux"
        },
        {
            libelle: "2837",
            libelle1: "Amont. bâtiments. industriels. concession",
            value: "2837 - Amont. bâtiments. industriels. concession"
        },
        {
            libelle: "2838",
            libelle1: "Amont. : autres. installations., agencements.",
            value: "2838 - Amont. : autres. installations., agencements."
        },
        {
            libelle: "284",
            libelle1: "Amortissements du matériel",
            value: "284 - Amortissements du matériel"
        },
        {
            libelle: "2841",
            libelle1: "Amont. mat-outillage industriels.",
            value: "2841 - Amont. mat-outillage industriels."
        },
        {
            libelle: "2842",
            libelle1: "Amont. mat-outillage agricole",
            value: "2842 - Amont. mat-outillage agricole"
        },
        {
            libelle: "2843",
            libelle1: "Amont. mat-outillage d'emballage",
            value: "2843 - Amont. mat-outillage d'emballage"
        },
        {
            libelle: "2844",
            libelle1: "Amortissements. matériel, mobilier",
            value: "2844 - Amortissements. matériel, mobilier"
        },
        {
            libelle: "2845",
            libelle1: "Amortissements. matériel transport",
            value: "2845 - Amortissements. matériel transport"
        },
        {
            libelle: "2846",
            libelle1: "Amont. : immobilisations. animales, agric.",
            value: "2846 - Amont. : immobilisations. animales, agric."
        },
        {
            libelle: "2847",
            libelle1: "Amont. : agencements., aménagement.",
            value: "2847 - Amont. : agencements., aménagement."
        },
        {
            libelle: "2848",
            libelle1: "Amortissements. : autres matériels",
            value: "2848 - Amortissements. : autres matériels"
        },
        {
            libelle: "29",
            libelle1: "Provisions pour dépréciation",
            value: "29 - Provisions pour dépréciation"
        },
        {
            libelle: "291",
            libelle1: "Provisions : immobilisations. incorporelles",
            value: "291 - Provisions : immobilisations. incorporelles"
        },
        {
            libelle: "2912",
            libelle1: "Provisions : brevets, licences",
            value: "2912 - Provisions : brevets, licences"
        },
        {
            libelle: "2913",
            libelle1: "Provisions des logiciels",
            value: "2913 - Provisions des logiciels"
        },
        {
            libelle: "2914",
            libelle1: "Provisions des marques",
            value: "2914 - Provisions des marques"
        },
        {
            libelle: "2915",
            libelle1: "Provisions du fonds commercial",
            value: "2915 - Provisions du fonds commercial"
        },
        {
            libelle: "2916",
            libelle1: "Provisions du droit au bail",
            value: "2916 - Provisions du droit au bail"
        },
        {
            libelle: "2917",
            libelle1: "Provisions : investissements. création",
            value: "2917 - Provisions : investissements. création"
        },
        {
            libelle: "2918",
            libelle1: "Provisions autres  valeurs incorporelles.",
            value: "2918 - Provisions autres  valeurs incorporelles."
        },
        {
            libelle: "2919",
            libelle1: "Provision Immobilisations incorporelles. En cours",
            value: "2919 - Provision Immobilisations incorporelles. En cours"
        },
        {
            libelle: "292",
            libelle1: "Provisions des terrains",
            value: "292 - Provisions des terrains"
        },
        {
            libelle: "293",
            libelle1: "Provisions : bâtiments, installations. ",
            value: "293 - Provisions : bâtiments, installations. "
        },
        {
            libelle: "2931",
            libelle1: "Provisions bâtiments. industriels. sol propre",
            value: "2931 - Provisions bâtiments. industriels. sol propre"
        },
        {
            libelle: "2932",
            libelle1: "Provisions bâtiments. industriels. sol autrui",
            value: "2932 - Provisions bâtiments. industriels. sol autrui"
        },
        {
            libelle: "2933",
            libelle1: "Provisions : ouvrages infrastructure",
            value: "2933 - Provisions : ouvrages infrastructure"
        },
        {
            libelle: "2934",
            libelle1: "Provisions : installations. techniques",
            value: "2934 - Provisions : installations. techniques"
        },
        {
            libelle: "2935",
            libelle1: "Provisions : aménagement. bureaux",
            value: "2935 - Provisions : aménagement. bureaux"
        },
        {
            libelle: "2937",
            libelle1: "Provisions bâtiments. industriels. concession",
            value: "2937 - Provisions bâtiments. industriels. concession"
        },
        {
            libelle: "2938",
            libelle1: "Provisions : autres. installations., agencements.",
            value: "2938 - Provisions : autres. installations., agencements."
        },
        {
            libelle: "2939",
            libelle1: "Provision Bâtiments En cours",
            value: "2939 - Provision Bâtiments En cours"
        },
        {
            libelle: "294",
            libelle1: "Provisions du matériel",
            value: "294 - Provisions du matériel"
        },
        {
            libelle: "2941",
            libelle1: "Provisions mat-outillage industriels.",
            value: "2941 - Provisions mat-outillage industriels."
        },
        {
            libelle: "2942",
            libelle1: "Provisions mat-outillage agricole",
            value: "2942 - Provisions mat-outillage agricole"
        },
        {
            libelle: "2943",
            libelle1: "Provisions mat-outillage d'emballage",
            value: "2943 - Provisions mat-outillage d'emballage"
        },
        {
            libelle: "2944",
            libelle1: "Provisions matériel, mobilier",
            value: "2944 - Provisions matériel, mobilier"
        },
        {
            libelle: "2945",
            libelle1: "Provisions matériel transport",
            value: "2945 - Provisions matériel transport"
        },
        {
            libelle: "2946",
            libelle1: "Provisions : immobilisations. animales, agric.",
            value: "2946 - Provisions : immobilisations. animales, agric."
        },
        {
            libelle: "2947",
            libelle1: "Provisions : agencements., aménagement.",
            value: "2947 - Provisions : agencements., aménagement."
        },
        {
            libelle: "2948",
            libelle1: "Provisions : autres matériels",
            value: "2948 - Provisions : autres matériels"
        },
        {
            libelle: "2949",
            libelle1: "Provision Matériel En cours",
            value: "2949 - Provision Matériel En cours"
        },
        {
            libelle: "295",
            libelle1: "Provisions avances et acomptes",
            value: "295 - Provisions avances et acomptes"
        },
        {
            libelle: "296",
            libelle1: "Provisions sut titres de participations",
            value: "296 - Provisions sut titres de participations"
        },
        {
            libelle: "297",
            libelle1: "Provisions sur autres immob.financières",
            value: "297 - Provisions sur autres immob.financières"
        },
        {
            libelle: "3",
            libelle1: "Comptes de stocks",
            value: "3 - Comptes de stocks"
        },
        {
            libelle: "31",
            libelle1: "Marchandises",
            value: "31 - Marchandises"
        },
        {
            libelle: "32",
            libelle1: "Matières premières, fournitures",
            value: "32 - Matières premières, fournitures"
        },
        {
            libelle: "33",
            libelle1: "Autres approvisionnements",
            value: "33 - Autres approvisionnements"
        },
        {
            libelle: "34",
            libelle1: "Produits en cours",
            value: "34 - Produits en cours"
        },
        {
            libelle: "35",
            libelle1: "Services en cours",
            value: "35 - Services en cours"
        },
        {
            libelle: "36",
            libelle1: "Produits finis",
            value: "36 - Produits finis"
        },
        {
            libelle: "37",
            libelle1: "Produits intermèdiaires., résiduels",
            value: "37 - Produits intermèdiaires., résiduels"
        },
        {
            libelle: "38",
            libelle1: "Stocks en cours de route",
            value: "38 - Stocks en cours de route"
        },
        {
            libelle: "381",
            libelle1: "Marchandises en cours de route",
            value: "381 - Marchandises en cours de route"
        },
        {
            libelle: "382",
            libelle1: "Mat. premières. en cours de route",
            value: "382 - Mat. premières. en cours de route"
        },
        {
            libelle: "383",
            libelle1: "Autres approvisionnements. en cours route",
            value: "383 - Autres approvisionnements. en cours route"
        },
        {
            libelle: "386",
            libelle1: "Produits finis en cours de route",
            value: "386 - Produits finis en cours de route"
        },
        {
            libelle: "387",
            libelle1: "Stock en consignation., en dépôt",
            value: "387 - Stock en consignation., en dépôt"
        },
        {
            libelle: "39",
            libelle1: "Dépréciations des stocks",
            value: "39 - Dépréciations des stocks"
        },
        {
            libelle: "391",
            libelle1: "Dépréciations. : stocks marchandises",
            value: "391 - Dépréciations. : stocks marchandises"
        },
        {
            libelle: "392",
            libelle1: "Dépréciations. : stocks mat. premières",
            value: "392 - Dépréciations. : stocks mat. premières"
        },
        {
            libelle: "393",
            libelle1: "Dépréciations. : stocks autres. approvisionnements.",
            value: "393 - Dépréciations. : stocks autres. approvisionnements."
        },
        {
            libelle: "394",
            libelle1: "Dépréciations. : produits en cours",
            value: "394 - Dépréciations. : produits en cours"
        },
        {
            libelle: "395",
            libelle1: "Dépréciations. : services en cours",
            value: "395 - Dépréciations. : services en cours"
        },
        {
            libelle: "396",
            libelle1: "Dépréciations. : stocks produits finis",
            value: "396 - Dépréciations. : stocks produits finis"
        },
        {
            libelle: "397",
            libelle1: "Dépréciations. : stocks produits intermèdiaires.",
            value: "397 - Dépréciations. : stocks produits intermèdiaires."
        },
        {
            libelle: "398",
            libelle1: "Dépréciations. : stocks cours de route",
            value: "398 - Dépréciations. : stocks cours de route"
        },
        {
            libelle: "4",
            libelle1: "Comptes de tiers",
            value: "4 - Comptes de tiers"
        },
        {
            libelle: "40",
            libelle1: "Fournisseurs, comptes rattachés",
            value: "40 - Fournisseurs, comptes rattachés"
        },
        {
            libelle: "401",
            libelle1: "Fournisseurs, dettes en compte",
            value: "401 - Fournisseurs, dettes en compte"
        },
        {
            libelle: "402",
            libelle1: "Fournisseurs, effets à payer",
            value: "402 - Fournisseurs, effets à payer"
        },
        {
            libelle: "408",
            libelle1: "Fournis., factures non parvenues",
            value: "408 - Fournis., factures non parvenues"
        },
        {
            libelle: "409",
            libelle1: "Fournisseurs débiteurs",
            value: "409 - Fournisseurs débiteurs"
        },
        {
            libelle: "41",
            libelle1: "Clients et comptes rattachés",
            value: "41 - Clients et comptes rattachés"
        },
        {
            libelle: "411",
            libelle1: "Clients",
            value: "411 - Clients"
        },
        {
            libelle: "412",
            libelle1: "Clients, effets à recevoir",
            value: "412 - Clients, effets à recevoir"
        },
        {
            libelle: "414",
            libelle1: "Créances Cessions. courantes immobilisations.",
            value: "414 - Créances Cessions. courantes immobilisations."
        },
        {
            libelle: "415",
            libelle1: "Clients effets. escomptés non échus",
            value: "415 - Clients effets. escomptés non échus"
        },
        {
            libelle: "416",
            libelle1: "Créances litigieuses douteuses",
            value: "416 - Créances litigieuses douteuses"
        },
        {
            libelle: "418",
            libelle1: "Clients, produits à recevoir",
            value: "418 - Clients, produits à recevoir"
        },
        {
            libelle: "419",
            libelle1: "Clients créditeurs",
            value: "419 - Clients créditeurs"
        },
        {
            libelle: "42",
            libelle1: "Personnel",
            value: "42 - Personnel"
        },
        {
            libelle: "421",
            libelle1: "Personnel, avances et acomptes",
            value: "421 - Personnel, avances et acomptes"
        },
        {
            libelle: "422",
            libelle1: "Personnel, rémunérations dues",
            value: "422 - Personnel, rémunérations dues"
        },
        {
            libelle: "423",
            libelle1: "Personnel, oppositions. saisies-arrêts",
            value: "423 - Personnel, oppositions. saisies-arrêts"
        },
        {
            libelle: "424",
            libelle1: "Personnel, œuvres sociales",
            value: "424 - Personnel, œuvres sociales"
        },
        {
            libelle: "425",
            libelle1: "Représentants du personnel",
            value: "425 - Représentants du personnel"
        },
        {
            libelle: "4281",
            libelle1: "Dettes provisionnées. congés à payer",
            value: "4281 - Dettes provisionnées. congés à payer"
        },
        {
            libelle: "4286",
            libelle1: "Pers., Autres charges à payer",
            value: "4286 - Pers., Autres charges à payer"
        },
        {
            libelle: "4287",
            libelle1: "Personnel, Produits à recevoir",
            value: "4287 - Personnel, Produits à recevoir"
        },
        {
            libelle: "43",
            libelle1: "Organismes sociaux",
            value: "43 - Organismes sociaux"
        },
        {
            libelle: "431",
            libelle1: "Sécurité sociale",
            value: "431 - Sécurité sociale"
        },
        {
            libelle: "433",
            libelle1: "Autres organismes sociaux",
            value: "433 - Autres organismes sociaux"
        },
        {
            libelle: "4386",
            libelle1: "Organismes. sociaux, Autres charges à payer",
            value: "4386 - Organismes. sociaux, Autres charges à payer"
        },
        {
            libelle: "4387",
            libelle1: "Organismes sociaux, Produits à recevoir",
            value: "4387 - Organismes sociaux, Produits à recevoir"
        },
        {
            libelle: "44",
            libelle1: "État et collectivités publiques",
            value: "44 - État et collectivités publiques"
        },
        {
            libelle: "441",
            libelle1: "État, impôt sur les bénéfices",
            value: "441 - État, impôt sur les bénéfices"
        },
        {
            libelle: "442",
            libelle1: "État, autres impôts et taxes",
            value: "442 - État, autres impôts et taxes"
        },
        {
            libelle: "443",
            libelle1: "État, TVA facturée",
            value: "443 - État, TVA facturée"
        },
        {
            libelle: "444",
            libelle1: "État, TVA due ou crédit de TVA",
            value: "444 - État, TVA due ou crédit de TVA"
        },
        {
            libelle: "445",
            libelle1: "État, TVA récupérable",
            value: "445 - État, TVA récupérable"
        },
        {
            libelle: "446",
            libelle1: "État, Autres taxes sur C.A.",
            value: "446 - État, Autres taxes sur C.A."
        },
        {
            libelle: "447",
            libelle1: "État, impôts retenus à la source",
            value: "447 - État, impôts retenus à la source"
        },
        {
            libelle: "4486",
            libelle1: "Etat, Charges à payer",
            value: "4486 - Etat, Charges à payer"
        },
        {
            libelle: "4487",
            libelle1: "Etat, Produits à recevoir",
            value: "4487 - Etat, Produits à recevoir"
        },
        {
            libelle: "449",
            libelle1: "État, créances, dettes diverses",
            value: "449 - État, créances, dettes diverses"
        },
        {
            libelle: "45",
            libelle1: "Organismes internationaux",
            value: "45 - Organismes internationaux"
        },
        {
            libelle: "451",
            libelle1: "Organismes africains",
            value: "451 - Organismes africains"
        },
        {
            libelle: "452",
            libelle1: "Autres organismes internationaux",
            value: "452 - Autres organismes internationaux"
        },
        {
            libelle: "4581",
            libelle1: "Organismes. int., fonds de dotation. à recevoir",
            value: "4581 - Organismes. int., fonds de dotation. à recevoir"
        },
        {
            libelle: "4582",
            libelle1: "Organismes. int., subvention à recevoir",
            value: "4582 - Organismes. int., subvention à recevoir"
        },
        {
            libelle: "46",
            libelle1: "Associés et groupe",
            value: "46 - Associés et groupe"
        },
        {
            libelle: "461",
            libelle1: "Associés, opérations en. / capital",
            value: "461 - Associés, opérations en. / capital"
        },
        {
            libelle: "462",
            libelle1: "Associés, comptes courants",
            value: "462 - Associés, comptes courants"
        },
        {
            libelle: "463",
            libelle1: "Associés, opérations en. en commun",
            value: "463 - Associés, opérations en. en commun"
        },
        {
            libelle: "465",
            libelle1: "Associés, dividendes à payer",
            value: "465 - Associés, dividendes à payer"
        },
        {
            libelle: "466",
            libelle1: "Groupe, comptes courants",
            value: "466 - Groupe, comptes courants"
        },
        {
            libelle: "467",
            libelle1: "Action., restant du Cal appelé",
            value: "467 - Action., restant du Cal appelé"
        },
        {
            libelle: "47",
            libelle1: "Débiteurs et créditeurs divers",
            value: "47 - Débiteurs et créditeurs divers"
        },
        {
            libelle: "4711",
            libelle1: "Débiteurs divers",
            value: "4711 - Débiteurs divers"
        },
        {
            libelle: "4712",
            libelle1: "Créditeurs divers",
            value: "4712 - Créditeurs divers"
        },
        {
            libelle: "472",
            libelle1: "Versements. restant à effectuer/titres non libérés",
            value: "472 - Versements. restant à effectuer/titres non libérés"
        },
        {
            libelle: "474",
            libelle1: "Répartition périodique",
            value: "474 - Répartition périodique"
        },
        {
            libelle: "475",
            libelle1: "Créances / Travaux non encore facturables",
            value: "475 - Créances / Travaux non encore facturables"
        },
        {
            libelle: "476",
            libelle1: "Charges constatées d'avance",
            value: "476 - Charges constatées d'avance"
        },
        {
            libelle: "477",
            libelle1: "Produits constatés d'avance",
            value: "477 - Produits constatés d'avance"
        },
        {
            libelle: "478",
            libelle1: "Écarts de conversion - actif",
            value: "478 - Écarts de conversion - actif"
        },
        {
            libelle: "4781",
            libelle1: "Diminution des créances",
            value: "4781 - Diminution des créances"
        },
        {
            libelle: "4782",
            libelle1: "Augmentation des dettes",
            value: "4782 - Augmentation des dettes"
        },
        {
            libelle: "4788",
            libelle1: "Différences. compens./couverture change",
            value: "4788 - Différences. compens./couverture change"
        },
        {
            libelle: "479",
            libelle1: "Écarts de conversion - passif",
            value: "479 - Écarts de conversion - passif"
        },
        {
            libelle: "4791",
            libelle1: "Augmentation des créances",
            value: "4791 - Augmentation des créances"
        },
        {
            libelle: "4792",
            libelle1: "Diminution des dettes",
            value: "4792 - Diminution des dettes"
        },
        {
            libelle: "4798",
            libelle1: "Différences. compens./couverture change",
            value: "4798 - Différences. compens./couverture change"
        },
        {
            libelle: "48",
            libelle1: "Créances et dettes  H.A.O.",
            value: "48 - Créances et dettes  H.A.O."
        },
        {
            libelle: "481",
            libelle1: "Fournisseurs d'investissements",
            value: "481 - Fournisseurs d'investissements"
        },
        {
            libelle: "482",
            libelle1: "Fournisseurs investissements., EAP",
            value: "482 - Fournisseurs investissements., EAP"
        },
        {
            libelle: "483",
            libelle1: "Dettes / acqu. titres placement",
            value: "483 - Dettes / acqu. titres placement"
        },
        {
            libelle: "484",
            libelle1: "Autres dettes H.A.O.",
            value: "484 - Autres dettes H.A.O."
        },
        {
            libelle: "485",
            libelle1: "Créances / cessions immobilisations.",
            value: "485 - Créances / cessions immobilisations."
        },
        {
            libelle: "486",
            libelle1: "Créances Cessions. titres placement",
            value: "486 - Créances Cessions. titres placement"
        },
        {
            libelle: "488",
            libelle1: "Autres créances H.A.O.",
            value: "488 - Autres créances H.A.O."
        },
        {
            libelle: "49",
            libelle1: "Dépréciations sur risques tiers",
            value: "49 - Dépréciations sur risques tiers"
        },
        {
            libelle: "490",
            libelle1: "Dépréciation : Comptes fournisseurs",
            value: "490 - Dépréciation : Comptes fournisseurs"
        },
        {
            libelle: "491",
            libelle1: "Dépréciation : Comptes clients",
            value: "491 - Dépréciation : Comptes clients"
        },
        {
            libelle: "492",
            libelle1: "Dépréciation : Comptes personnel",
            value: "492 - Dépréciation : Comptes personnel"
        },
        {
            libelle: "493",
            libelle1: "Dépréciation : Comptes organismes sociaux",
            value: "493 - Dépréciation : Comptes organismes sociaux"
        },
        {
            libelle: "494",
            libelle1: "Dépréciation : Comptes d'État et collectivités publiques",
            value: "494 - Dépréciation : Comptes d'État et collectivités publiques"
        },
        {
            libelle: "495",
            libelle1: "Dépréciation : Comptes organismes internationaux",
            value: "495 - Dépréciation : Comptes organismes internationaux"
        },
        {
            libelle: "496",
            libelle1: "Dépréciation : Comptes associé-groupe",
            value: "496 - Dépréciation : Comptes associé-groupe"
        },
        {
            libelle: "497",
            libelle1: "Dépréciation : Comptes débiteurs divers",
            value: "497 - Dépréciation : Comptes débiteurs divers"
        },
        {
            libelle: "498",
            libelle1: "Dépréciation : Comptes de créances H.A.O.",
            value: "498 - Dépréciation : Comptes de créances H.A.O."
        },
        {
            libelle: "4981",
            libelle1: "Dépréciation créances sur cessions d'immobilisations",
            value: "4981 - Dépréciation créances sur cessions d'immobilisations"
        },
        {
            libelle: "4982",
            libelle1: "Dépréciation créances sur cessions de titres placement",
            value: "4982 - Dépréciation créances sur cessions de titres placement"
        },
        {
            libelle: "4983",
            libelle1: "Dépréciation Autres créances H.A.O.",
            value: "4983 - Dépréciation Autres créances H.A.O."
        },
        {
            libelle: "499",
            libelle1: "Risques provisionnés",
            value: "499 - Risques provisionnés"
        },
        {
            libelle: "4991",
            libelle1: "Risques provisionnés sur opérations d'exploitation",
            value: "4991 - Risques provisionnés sur opérations d'exploitation"
        },
        {
            libelle: "4998",
            libelle1: "Risques provisionnés sur opérations H.A.O.",
            value: "4998 - Risques provisionnés sur opérations H.A.O."
        },
        {
            libelle: "5",
            libelle1: "Comptes de trésorerie",
            value: "5 - Comptes de trésorerie"
        },
        {
            libelle: "50",
            libelle1: "Titres de placement",
            value: "50 - Titres de placement"
        },
        {
            libelle: "501",
            libelle1: "Titres du trésor, bons caisse CT",
            value: "501 - Titres du trésor, bons caisse CT"
        },
        {
            libelle: "502",
            libelle1: "Actions",
            value: "502 - Actions"
        },
        {
            libelle: "503",
            libelle1: "Obligations",
            value: "503 - Obligations"
        },
        {
            libelle: "504",
            libelle1: "Bons de souscription",
            value: "504 - Bons de souscription"
        },
        {
            libelle: "51",
            libelle1: "Valeurs à encaisser",
            value: "51 - Valeurs à encaisser"
        },
        {
            libelle: "52",
            libelle1: "Banques",
            value: "52 - Banques"
        },
        {
            libelle: "5211",
            libelle1: "Banques débitrices",
            value: "5211 - Banques débitrices"
        },
        {
            libelle: "5212",
            libelle1: "Banque créditrices",
            value: "5212 - Banque créditrices"
        },
        {
            libelle: "522",
            libelle1: "Banques autres états UÉMOA",
            value: "522 - Banques autres états UÉMOA"
        },
        {
            libelle: "523",
            libelle1: "Banques autres états Zone Franc",
            value: "523 - Banques autres états Zone Franc"
        },
        {
            libelle: "524",
            libelle1: "Banques hors Zone Franc",
            value: "524 - Banques hors Zone Franc"
        },
        {
            libelle: "526",
            libelle1: "Intérêts courus sur crédits bancaires",
            value: "526 - Intérêts courus sur crédits bancaires"
        },
        {
            libelle: "53",
            libelle1: "Établisst financiers, assimilés",
            value: "53 - Établisst financiers, assimilés"
        },
        {
            libelle: "54",
            libelle1: "Instruments de trésorerie",
            value: "54 - Instruments de trésorerie"
        },
        {
            libelle: "541",
            libelle1: "Options de taux d'intérêt",
            value: "541 - Options de taux d'intérêt"
        },
        {
            libelle: "542",
            libelle1: "Options de taux de change",
            value: "542 - Options de taux de change"
        },
        {
            libelle: "543",
            libelle1: "Options de taux boursiers",
            value: "543 - Options de taux boursiers"
        },
        {
            libelle: "544",
            libelle1: "Instruments de marchés à terme",
            value: "544 - Instruments de marchés à terme"
        },
        {
            libelle: "545",
            libelle1: "Avoirs or, autres. métaux précieux",
            value: "545 - Avoirs or, autres. métaux précieux"
        },
        {
            libelle: "56",
            libelle1: "Banques, crédits de trésorerie, escompte",
            value: "56 - Banques, crédits de trésorerie, escompte"
        },
        {
            libelle: "561",
            libelle1: "Crédits de trésorerie",
            value: "561 - Crédits de trésorerie"
        },
        {
            libelle: "564",
            libelle1: "Escompte de crédits de campagne",
            value: "564 - Escompte de crédits de campagne"
        },
        {
            libelle: "565",
            libelle1: "Escompte de crédits ordinaires",
            value: "565 - Escompte de crédits ordinaires"
        },
        {
            libelle: "566",
            libelle1: "Intérêts courus sur crédits de trésorerie et escompte",
            value: "566 - Intérêts courus sur crédits de trésorerie et escompte"
        },
        {
            libelle: "57",
            libelle1: "Caisse",
            value: "57 - Caisse"
        },
        {
            libelle: "58",
            libelle1: "Régies d'avances, accréditifs",
            value: "58 - Régies d'avances, accréditifs"
        },
        {
            libelle: "59",
            libelle1: "Dépréciations. risques trésorerie",
            value: "59 - Dépréciations. risques trésorerie"
        },
        {
            libelle: "590",
            libelle1: "Dépréciations. Risques Titres de placements",
            value: "590 - Dépréciations. Risques Titres de placements"
        },
        {
            libelle: "591",
            libelle1: "Dépréciations. Risques Valeurs à encaisser",
            value: "591 - Dépréciations. Risques Valeurs à encaisser"
        },
        {
            libelle: "592",
            libelle1: "Dépréciations. Autres risques de trésorerie",
            value: "592 - Dépréciations. Autres risques de trésorerie"
        },
        {
            libelle: "6",
            libelle1: "Comptes de charges (A.O.)",
            value: "6 - Comptes de charges (A.O.)"
        },
        {
            libelle: "60",
            libelle1: "Achats et variations de stocks",
            value: "60 - Achats et variations de stocks"
        },
        {
            libelle: "601",
            libelle1: "Achats de marchandises",
            value: "601 - Achats de marchandises"
        },
        {
            libelle: "602",
            libelle1: "Achats Mat. premières, fournitures.",
            value: "602 - Achats Mat. premières, fournitures."
        },
        {
            libelle: "6021",
            libelle1: "MP et fournitures. dans l'UÉMOA",
            value: "6021 - MP et fournitures. dans l'UÉMOA"
        },
        {
            libelle: "6022",
            libelle1: "MP et fournitures. hors UÉMOA",
            value: "6022 - MP et fournitures. hors UÉMOA"
        },
        {
            libelle: "6023",
            libelle1: "MP et fournitures. Entrep. du groupe dans l'UÉMOA",
            value: "6023 - MP et fournitures. Entrep. du groupe dans l'UÉMOA"
        },
        {
            libelle: "6024",
            libelle1: "MP et fournitures. Entreprises du groupe hors UÉMOA",
            value: "6024 - MP et fournitures. Entreprises du groupe hors UÉMOA"
        },
        {
            libelle: "6029",
            libelle1: "MP et fournitures. Rabais, remises, ristournes. obtenus",
            value: "6029 - MP et fournitures. Rabais, remises, ristournes. obtenus"
        },
        {
            libelle: "603",
            libelle1: "Variations. : stocks biens achetés",
            value: "603 - Variations. : stocks biens achetés"
        },
        {
            libelle: "6031",
            libelle1: "Variations : stocks marchandises",
            value: "6031 - Variations : stocks marchandises"
        },
        {
            libelle: "6032",
            libelle1: "Variations. Mat. premières, fournit.",
            value: "6032 - Variations. Mat. premières, fournit."
        },
        {
            libelle: "6033",
            libelle1: "Variations. Autres approvisionnement.",
            value: "6033 - Variations. Autres approvisionnement."
        },
        {
            libelle: "604",
            libelle1: "Achats stockés de matières et fournitures",
            value: "604 - Achats stockés de matières et fournitures"
        },
        {
            libelle: "605",
            libelle1: "Autres achats",
            value: "605 - Autres achats"
        },
        {
            libelle: "6051",
            libelle1: "Fournitures non stockables - eau",
            value: "6051 - Fournitures non stockables - eau"
        },
        {
            libelle: "6052",
            libelle1: "Électricité",
            value: "6052 - Électricité"
        },
        {
            libelle: "6053",
            libelle1: "Autres énergies",
            value: "6053 - Autres énergies"
        },
        {
            libelle: "6054",
            libelle1: "Fournitures entretien",
            value: "6054 - Fournitures entretien"
        },
        {
            libelle: "6055",
            libelle1: "Fournit. bureau non stockables",
            value: "6055 - Fournit. bureau non stockables"
        },
        {
            libelle: "6056",
            libelle1: "Achats petit matériel, outillage",
            value: "6056 - Achats petit matériel, outillage"
        },
        {
            libelle: "6057",
            libelle1: "Achats études, prestations de. service",
            value: "6057 - Achats études, prestations de. service"
        },
        {
            libelle: "6058",
            libelle1: "Achats travaux, matériel, équipement.",
            value: "6058 - Achats travaux, matériel, équipement."
        },
        {
            libelle: "6059",
            libelle1: "Rabais, remises, ristournes. obtenus",
            value: "6059 - Rabais, remises, ristournes. obtenus"
        },
        {
            libelle: "608",
            libelle1: "Achats d'emballages",
            value: "608 - Achats d'emballages"
        },
        {
            libelle: "61",
            libelle1: "Transports",
            value: "61 - Transports"
        },
        {
            libelle: "611",
            libelle1: "Transports sur achats",
            value: "611 - Transports sur achats"
        },
        {
            libelle: "612",
            libelle1: "Transports sur ventes",
            value: "612 - Transports sur ventes"
        },
        {
            libelle: "613",
            libelle1: "Transports pour le compte tiers",
            value: "613 - Transports pour le compte tiers"
        },
        {
            libelle: "614",
            libelle1: "Transports du personnel",
            value: "614 - Transports du personnel"
        },
        {
            libelle: "618",
            libelle1: "Autres frais de transport",
            value: "618 - Autres frais de transport"
        },
        {
            libelle: "62 et 63",
            libelle1: "Services extérieurs A et B",
            value: "62 et 63 - Services extérieurs A et B"
        },
        {
            libelle: "621",
            libelle1: "Sous-traitance générale",
            value: "621 - Sous-traitance générale"
        },
        {
            libelle: "622",
            libelle1: "Locations et charges locatives",
            value: "622 - Locations et charges locatives"
        },
        {
            libelle: "623",
            libelle1: "Redevances crédit-bail et assimilées.",
            value: "623 - Redevances crédit-bail et assimilées."
        },
        {
            libelle: "6232",
            libelle1: "Crédit-bail immobilier",
            value: "6232 - Crédit-bail immobilier"
        },
        {
            libelle: "6233",
            libelle1: "Crédit-bail mobilier",
            value: "6233 - Crédit-bail mobilier"
        },
        {
            libelle: "6235",
            libelle1: "Contrats assimilés",
            value: "6235 - Contrats assimilés"
        },
        {
            libelle: "624",
            libelle1: "Entretien, réparat., maintenance",
            value: "624 - Entretien, réparat., maintenance"
        },
        {
            libelle: "6241",
            libelle1: "Entretien, réparat. biens immobilisations.",
            value: "6241 - Entretien, réparat. biens immobilisations."
        },
        {
            libelle: "6242",
            libelle1: "Entretien, rép. biens mobiliers",
            value: "6242 - Entretien, rép. biens mobiliers"
        },
        {
            libelle: "6243",
            libelle1: "Maintenance",
            value: "6243 - Maintenance"
        },
        {
            libelle: "6248",
            libelle1: "Autres entretiens et réparations",
            value: "6248 - Autres entretiens et réparations"
        },
        {
            libelle: "625",
            libelle1: "Primes d'assurance",
            value: "625 - Primes d'assurance"
        },
        {
            libelle: "626",
            libelle1: "Études, recherches, documentation.",
            value: "626 - Études, recherches, documentation."
        },
        {
            libelle: "627",
            libelle1: "Publicité et publications",
            value: "627 - Publicité et publications"
        },
        {
            libelle: "628",
            libelle1: "Frais de télécommunications",
            value: "628 - Frais de télécommunications"
        },
        {
            libelle: "63",
            libelle1: "Services extérieurs B",
            value: "63 - Services extérieurs B"
        },
        {
            libelle: "631",
            libelle1: "Frais bancaires",
            value: "631 - Frais bancaires"
        },
        {
            libelle: "632",
            libelle1: "Rémunérations. intermèdiaires., conseils",
            value: "632 - Rémunérations. intermèdiaires., conseils"
        },
        {
            libelle: "633",
            libelle1: "Frais de formation du personnel",
            value: "633 - Frais de formation du personnel"
        },
        {
            libelle: "634",
            libelle1: "Redevances brevets, licences",
            value: "634 - Redevances brevets, licences"
        },
        {
            libelle: "6342",
            libelle1: "Redevances brevets, licences",
            value: "6342 - Redevances brevets, licences"
        },
        {
            libelle: "6343",
            libelle1: "Redevances pour logiciels",
            value: "6343 - Redevances pour logiciels"
        },
        {
            libelle: "6344",
            libelle1: "Redevances pour marques",
            value: "6344 - Redevances pour marques"
        },
        {
            libelle: "635",
            libelle1: "Cotisations",
            value: "635 - Cotisations"
        },
        {
            libelle: "6351",
            libelle1: "Cotisations",
            value: "6351 - Cotisations"
        },
        {
            libelle: "6358",
            libelle1: "Concours divers",
            value: "6358 - Concours divers"
        },
        {
            libelle: "637",
            libelle1: "Rémunérations. personnel extérieur",
            value: "637 - Rémunérations. personnel extérieur"
        },
        {
            libelle: "6371",
            libelle1: "Personnel intérimaire",
            value: "6371 - Personnel intérimaire"
        },
        {
            libelle: "6372",
            libelle1: "Personnel détaché ou prêté",
            value: "6372 - Personnel détaché ou prêté"
        },
        {
            libelle: "638",
            libelle1: "Autres charges externes",
            value: "638 - Autres charges externes"
        },
        {
            libelle: "64",
            libelle1: "Impôts et taxes",
            value: "64 - Impôts et taxes"
        },
        {
            libelle: "641",
            libelle1: "Impôts et taxes directs",
            value: "641 - Impôts et taxes directs"
        },
        {
            libelle: "6411",
            libelle1: "Impôts fonciers et taxes annexes",
            value: "6411 - Impôts fonciers et taxes annexes"
        },
        {
            libelle: "6412",
            libelle1: "Patentes-licences, taxes annexes",
            value: "6412 - Patentes-licences, taxes annexes"
        },
        {
            libelle: "6413",
            libelle1: "Taxes / appointements, salaires",
            value: "6413 - Taxes / appointements, salaires"
        },
        {
            libelle: "6414",
            libelle1: "Taxes d'apprentissage",
            value: "6414 - Taxes d'apprentissage"
        },
        {
            libelle: "6415",
            libelle1: "Format. professionnelle continue",
            value: "6415 - Format. professionnelle continue"
        },
        {
            libelle: "6418",
            libelle1: "Autres impôts et taxes directs",
            value: "6418 - Autres impôts et taxes directs"
        },
        {
            libelle: "645",
            libelle1: "Impôts et taxes indirects",
            value: "645 - Impôts et taxes indirects"
        },
        {
            libelle: "646",
            libelle1: "Droits d'enregistrement",
            value: "646 - Droits d'enregistrement"
        },
        {
            libelle: "6461",
            libelle1: "Droits de mutation",
            value: "6461 - Droits de mutation"
        },
        {
            libelle: "6462",
            libelle1: "Droits de timbre",
            value: "6462 - Droits de timbre"
        },
        {
            libelle: "6463",
            libelle1: "Taxes / les véhicules société",
            value: "6463 - Taxes / les véhicules société"
        },
        {
            libelle: "6464",
            libelle1: "Vignettes",
            value: "6464 - Vignettes"
        },
        {
            libelle: "6468",
            libelle1: "Autres droits",
            value: "6468 - Autres droits"
        },
        {
            libelle: "647",
            libelle1: "Pénalités et amendes fiscales",
            value: "647 - Pénalités et amendes fiscales"
        },
        {
            libelle: "65",
            libelle1: "Autres charges",
            value: "65 - Autres charges"
        },
        {
            libelle: "651",
            libelle1: "Pertes Créances clients et autres.",
            value: "651 - Pertes Créances clients et autres."
        },
        {
            libelle: "652",
            libelle1: "QP résultat / opérations en. en commun",
            value: "652 - QP résultat / opérations en. en commun"
        },
        {
            libelle: "6521",
            libelle1: "Quote-part transférée bénéfices",
            value: "6521 - Quote-part transférée bénéfices"
        },
        {
            libelle: "6525",
            libelle1: "Pertes imputées par transfert",
            value: "6525 - Pertes imputées par transfert"
        },
        {
            libelle: "653",
            libelle1: "QP résult.annul./exécution. partiel",
            value: "653 - QP résult.annul./exécution. partiel"
        },
        {
            libelle: "654",
            libelle1: "Val comptable cession courante immobilisations",
            value: "654 - Val comptable cession courante immobilisations"
        },
        {
            libelle: "65411",
            libelle1: "Valeur Brute Immobilisations incorporelles",
            value: "65411 - Valeur Brute Immobilisations incorporelles"
        },
        {
            libelle: "65418",
            libelle1: "Amont. Immobilisations incorporelles",
            value: "65418 - Amont. Immobilisations incorporelles"
        },
        {
            libelle: "65421",
            libelle1: "Valeur Brute Immobilisations corporelles",
            value: "65421 - Valeur Brute Immobilisations corporelles"
        },
        {
            libelle: "65428",
            libelle1: "Amont. Immobilisations corporelles",
            value: "65428 - Amont. Immobilisations corporelles"
        },
        {
            libelle: "65461",
            libelle1: "Valeur Brute Immobilisations financières",
            value: "65461 - Valeur Brute Immobilisations financières"
        },
        {
            libelle: "65468",
            libelle1: "Amont. Immobilisations financières",
            value: "65468 - Amont. Immobilisations financières"
        },
        {
            libelle: "658",
            libelle1: "Charges diverses",
            value: "658 - Charges diverses"
        },
        {
            libelle: "6581",
            libelle1: "Jetons présence, autres rémunération administrateur.",
            value: "6581 - Jetons présence, autres rémunération administrateur."
        },
        {
            libelle: "6582",
            libelle1: "Dons",
            value: "6582 - Dons"
        },
        {
            libelle: "6583",
            libelle1: "Mécénat",
            value: "6583 - Mécénat"
        },
        {
            libelle: "659",
            libelle1: "Charges provisionnées exploitation.",
            value: "659 - Charges provisionnées exploitation."
        },
        {
            libelle: "6591",
            libelle1: "Sur risques à court terme",
            value: "6591 - Sur risques à court terme"
        },
        {
            libelle: "6593",
            libelle1: "Sur stocks",
            value: "6593 - Sur stocks"
        },
        {
            libelle: "6594",
            libelle1: "Sur créances",
            value: "6594 - Sur créances"
        },
        {
            libelle: "6598",
            libelle1: "Autres charges provisionnées",
            value: "6598 - Autres charges provisionnées"
        },
        {
            libelle: "66",
            libelle1: "Charges de personnel",
            value: "66 - Charges de personnel"
        },
        {
            libelle: "661",
            libelle1: "Rémunérations personnel national",
            value: "661 - Rémunérations personnel national"
        },
        {
            libelle: "6611",
            libelle1: "Appointements., salaires, commissions.",
            value: "6611 - Appointements., salaires, commissions."
        },
        {
            libelle: "6612",
            libelle1: "Primes et gratifications",
            value: "6612 - Primes et gratifications"
        },
        {
            libelle: "6613",
            libelle1: "Congés payés",
            value: "6613 - Congés payés"
        },
        {
            libelle: "6614",
            libelle1: "Indemnités préavis, licenciement",
            value: "6614 - Indemnités préavis, licenciement"
        },
        {
            libelle: "6615",
            libelle1: "Indemnités. maladie versées travailleur",
            value: "6615 - Indemnités. maladie versées travailleur"
        },
        {
            libelle: "6616",
            libelle1: "Supplément familial",
            value: "6616 - Supplément familial"
        },
        {
            libelle: "6617",
            libelle1: "Avantages en nature",
            value: "6617 - Avantages en nature"
        },
        {
            libelle: "6618",
            libelle1: "Autres rémunérations directes",
            value: "6618 - Autres rémunérations directes"
        },
        {
            libelle: "662",
            libelle1: "Rémunèrations. personnel non national",
            value: "662 - Rémunèrations. personnel non national"
        },
        {
            libelle: "6621",
            libelle1: "Appointements., salaires, commissions.",
            value: "6621 - Appointements., salaires, commissions."
        },
        {
            libelle: "6622",
            libelle1: "Primes et gratifications",
            value: "6622 - Primes et gratifications"
        },
        {
            libelle: "6623",
            libelle1: "Congés payés",
            value: "6623 - Congés payés"
        },
        {
            libelle: "6624",
            libelle1: "Indemnités préavis, licenciement",
            value: "6624 - Indemnités préavis, licenciement"
        },
        {
            libelle: "6625",
            libelle1: "Indemnités. maladie versées travailleur",
            value: "6625 - Indemnités. maladie versées travailleur"
        },
        {
            libelle: "6626",
            libelle1: "Supplément familial",
            value: "6626 - Supplément familial"
        },
        {
            libelle: "6627",
            libelle1: "Avantages en nature",
            value: "6627 - Avantages en nature"
        },
        {
            libelle: "6628",
            libelle1: "Autres rémunérations directes",
            value: "6628 - Autres rémunérations directes"
        },
        {
            libelle: "663",
            libelle1: "Indemnités. forfaitaires versées",
            value: "663 - Indemnités. forfaitaires versées"
        },
        {
            libelle: "664",
            libelle1: "Charges sociales",
            value: "664 - Charges sociales"
        },
        {
            libelle: "6641",
            libelle1: "Ch. sociales /personnel national",
            value: "6641 - Ch. sociales /personnel national"
        },
        {
            libelle: "6642",
            libelle1: "Ch. soc. /personnel non national",
            value: "6642 - Ch. soc. /personnel non national"
        },
        {
            libelle: "666",
            libelle1: "Rémunérations. exploitant individuel",
            value: "666 - Rémunérations. exploitant individuel"
        },
        {
            libelle: "6661",
            libelle1: "Rémunérations. travail l'exploitant",
            value: "6661 - Rémunérations. travail l'exploitant"
        },
        {
            libelle: "6662",
            libelle1: "Charges sociales",
            value: "6662 - Charges sociales"
        },
        {
            libelle: "667",
            libelle1: "Rémunérations. transférée personnel extérieur.",
            value: "667 - Rémunérations. transférée personnel extérieur."
        },
        {
            libelle: "6671",
            libelle1: "Personnel intérimaire",
            value: "6671 - Personnel intérimaire"
        },
        {
            libelle: "6672",
            libelle1: "Personnel détaché ou prêté",
            value: "6672 - Personnel détaché ou prêté"
        },
        {
            libelle: "668",
            libelle1: "Autres charges sociales",
            value: "668 - Autres charges sociales"
        },
        {
            libelle: "67",
            libelle1: "Frais financiers, charges assimilées.",
            value: "67 - Frais financiers, charges assimilées."
        },
        {
            libelle: "671",
            libelle1: "Intérêts des emprunts",
            value: "671 - Intérêts des emprunts"
        },
        {
            libelle: "672",
            libelle1: "Intérêts loyers crédit-bail",
            value: "672 - Intérêts loyers crédit-bail"
        },
        {
            libelle: "6721",
            libelle1: "Intérêts loyer C-bail immobilier",
            value: "6721 - Intérêts loyer C-bail immobilier"
        },
        {
            libelle: "6722",
            libelle1: "Intérêts loyer C-bail mobilier",
            value: "6722 - Intérêts loyer C-bail mobilier"
        },
        {
            libelle: "6723",
            libelle1: "Intérêts loyers :autres contrats",
            value: "6723 - Intérêts loyers :autres contrats"
        },
        {
            libelle: "673",
            libelle1: "Escomptes accordés",
            value: "673 - Escomptes accordés"
        },
        {
            libelle: "674",
            libelle1: "Autres intérêts",
            value: "674 - Autres intérêts"
        },
        {
            libelle: "676",
            libelle1: "Pertes de change",
            value: "676 - Pertes de change"
        },
        {
            libelle: "677",
            libelle1: "Pertes sur cessions de titres placement",
            value: "677 - Pertes sur cessions de titres placement"
        },
        {
            libelle: "678",
            libelle1: "Pertes sur risques financiers",
            value: "678 - Pertes sur risques financiers"
        },
        {
            libelle: "6781",
            libelle1: "Sur rentes viagères",
            value: "6781 - Sur rentes viagères"
        },
        {
            libelle: "6782",
            libelle1: "Sur opérations financières",
            value: "6782 - Sur opérations financières"
        },
        {
            libelle: "6784",
            libelle1: "Sur instruments de trésorerie",
            value: "6784 - Sur instruments de trésorerie"
        },
        {
            libelle: "679",
            libelle1: "Charges provisionnées financière",
            value: "679 - Charges provisionnées financière"
        },
        {
            libelle: "6791",
            libelle1: "Sur risques financiers",
            value: "6791 - Sur risques financiers"
        },
        {
            libelle: "6795",
            libelle1: "Sur titres de placement",
            value: "6795 - Sur titres de placement"
        },
        {
            libelle: "6798",
            libelle1: "Autres. charges provisionnées. financières",
            value: "6798 - Autres. charges provisionnées. financières"
        },
        {
            libelle: "68",
            libelle1: "Dotations aux amortissements",
            value: "68 - Dotations aux amortissements"
        },
        {
            libelle: "681",
            libelle1: "Dotations amortissements d'exploitation",
            value: "681 - Dotations amortissements d'exploitation"
        },
        {
            libelle: "6811",
            libelle1: "Dotations. amort. : Charges immobilisées",
            value: "6811 - Dotations. amort. : Charges immobilisées"
        },
        {
            libelle: "68121",
            libelle1: "Dotations. amort. : Frais R&D",
            value: "68121 - Dotations. amort. : Frais R&D"
        },
        {
            libelle: "68122",
            libelle1: "Dotations. amort. : Brevets,licences",
            value: "68122 - Dotations. amort. : Brevets,licences"
        },
        {
            libelle: "68125",
            libelle1: "Dotations. amort. : Fonds commercial",
            value: "68125 - Dotations. amort. : Fonds commercial"
        },
        {
            libelle: "68127",
            libelle1: "Dotations. amort. : autres immobilisations. incorporelles.",
            value: "68127 - Dotations. amort. : autres immobilisations. incorporelles."
        },
        {
            libelle: "68131",
            libelle1: "Dotations. amort. : Terrains",
            value: "68131 - Dotations. amort. : Terrains"
        },
        {
            libelle: "68132",
            libelle1: "Dotations. amort. : Bâtiments",
            value: "68132 - Dotations. amort. : Bâtiments"
        },
        {
            libelle: "68133",
            libelle1: "Dotations. amort. : AAI",
            value: "68133 - Dotations. amort. : AAI"
        },
        {
            libelle: "68134",
            libelle1: "Dotations. amort. : Matériel",
            value: "68134 - Dotations. amort. : Matériel"
        },
        {
            libelle: "68135",
            libelle1: "Dotations. amort. : Transport",
            value: "68135 - Dotations. amort. : Transport"
        },
        {
            libelle: "687",
            libelle1: "Dot. amort.à caractère financier",
            value: "687 - Dot. amort.à caractère financier"
        },
        {
            libelle: "6872",
            libelle1: "Dotat. amort. P.R.Oblig.",
            value: "6872 - Dotat. amort. P.R.Oblig."
        },
        {
            libelle: "6878",
            libelle1: "Aut. dotat. amort. financières",
            value: "6878 - Aut. dotat. amort. financières"
        },
        {
            libelle: "69",
            libelle1: "Dotations aux provisions",
            value: "69 - Dotations aux provisions"
        },
        {
            libelle: "691",
            libelle1: "Dotat. aux provisions exploitat.",
            value: "691 - Dotat. aux provisions exploitat."
        },
        {
            libelle: "6911",
            libelle1: "Pour risques et charges",
            value: "6911 - Pour risques et charges"
        },
        {
            libelle: "6912",
            libelle1: "Pour grosses réparations",
            value: "6912 - Pour grosses réparations"
        },
        {
            libelle: "6913",
            libelle1: "Dépréciat. : immob. incorporel.",
            value: "6913 - Dépréciat. : immob. incorporel."
        },
        {
            libelle: "6914",
            libelle1: "Dépréciat. : immob. corporelles",
            value: "6914 - Dépréciat. : immob. corporelles"
        },
        {
            libelle: "697",
            libelle1: "Dotat. aux provis. financières",
            value: "697 - Dotat. aux provis. financières"
        },
        {
            libelle: "6971",
            libelle1: "Pour risques et charges",
            value: "6971 - Pour risques et charges"
        },
        {
            libelle: "6972",
            libelle1: "Dépréciat. : immob. financières",
            value: "6972 - Dépréciat. : immob. financières"
        },
        {
            libelle: "7",
            libelle1: "Comptes de produits (A.O.)",
            value: "7 - Comptes de produits (A.O.)"
        },
        {
            libelle: "70",
            libelle1: "Ventes",
            value: "70 - Ventes"
        },
        {
            libelle: "701",
            libelle1: "Ventes de marchandises",
            value: "701 - Ventes de marchandises"
        },
        {
            libelle: "702",
            libelle1: "Ventes de produits finis",
            value: "702 - Ventes de produits finis"
        },
        {
            libelle: "7021",
            libelle1: "Produits finis dans l'UÉMOA",
            value: "7021 - Produits finis dans l'UÉMOA"
        },
        {
            libelle: "7022",
            libelle1: "Produits finis Hors UÉMOA",
            value: "7022 - Produits finis Hors UÉMOA"
        },
        {
            libelle: "7023",
            libelle1: "Produits finis Groupe UÉMOA",
            value: "7023 - Produits finis Groupe UÉMOA"
        },
        {
            libelle: "7024",
            libelle1: "Produits finis Groupe hors UÉMOA",
            value: "7024 - Produits finis Groupe hors UÉMOA"
        },
        {
            libelle: "703",
            libelle1: "Ventes produits intermédiaires",
            value: "703 - Ventes produits intermédiaires"
        },
        {
            libelle: "7031",
            libelle1: "Produits interm. dans l'UÉMOA",
            value: "7031 - Produits interm. dans l'UÉMOA"
        },
        {
            libelle: "7032",
            libelle1: "Produits interm. Hors UÉMOA",
            value: "7032 - Produits interm. Hors UÉMOA"
        },
        {
            libelle: "7033",
            libelle1: "Produits interm. Groupe UÉMOA",
            value: "7033 - Produits interm. Groupe UÉMOA"
        },
        {
            libelle: "7034",
            libelle1: "Prodts interm. Groupe hors UÉMOA",
            value: "7034 - Prodts interm. Groupe hors UÉMOA"
        },
        {
            libelle: "704",
            libelle1: "Ventes de produits résiduels",
            value: "704 - Ventes de produits résiduels"
        },
        {
            libelle: "7041",
            libelle1: "Produits résiduels dans l'UÉMOA",
            value: "7041 - Produits résiduels dans l'UÉMOA"
        },
        {
            libelle: "7042",
            libelle1: "Produits résiduels Hors UÉMOA",
            value: "7042 - Produits résiduels Hors UÉMOA"
        },
        {
            libelle: "7043",
            libelle1: "Produits résiduels Groupe UÉMOA",
            value: "7043 - Produits résiduels Groupe UÉMOA"
        },
        {
            libelle: "7044",
            libelle1: "Prodts résidu. Groupe hors UÉMOA",
            value: "7044 - Prodts résidu. Groupe hors UÉMOA"
        },
        {
            libelle: "705",
            libelle1: "Travaux facturés",
            value: "705 - Travaux facturés"
        },
        {
            libelle: "7051",
            libelle1: "Travaux dans l'UÉMOA",
            value: "7051 - Travaux dans l'UÉMOA"
        },
        {
            libelle: "7052",
            libelle1: "Travaux Hors UÉMOA",
            value: "7052 - Travaux Hors UÉMOA"
        },
        {
            libelle: "7053",
            libelle1: "Travaux Groupe UÉMOA",
            value: "7053 - Travaux Groupe UÉMOA"
        },
        {
            libelle: "7054",
            libelle1: "Travaux Groupe hors UÉMOA",
            value: "7054 - Travaux Groupe hors UÉMOA"
        },
        {
            libelle: "706",
            libelle1: "Services vendus",
            value: "706 - Services vendus"
        },
        {
            libelle: "7061",
            libelle1: "Services vendus dans l'UÉMOA",
            value: "7061 - Services vendus dans l'UÉMOA"
        },
        {
            libelle: "7062",
            libelle1: "Services vendus Hors UÉMOA",
            value: "7062 - Services vendus Hors UÉMOA"
        },
        {
            libelle: "7063",
            libelle1: "Services vendus Groupe UÉMOA",
            value: "7063 - Services vendus Groupe UÉMOA"
        },
        {
            libelle: "7064",
            libelle1: "Services vendus Groupe hors UÉMOA",
            value: "7064 - Services vendus Groupe hors UÉMOA"
        },
        {
            libelle: "707",
            libelle1: "Produits accessoires",
            value: "707 - Produits accessoires"
        },
        {
            libelle: "7071",
            libelle1: "Ports, emballagas perdus, autres frais",
            value: "7071 - Ports, emballagas perdus, autres frais"
        },
        {
            libelle: "7072",
            libelle1: "Commissions et courtages",
            value: "7072 - Commissions et courtages"
        },
        {
            libelle: "7073",
            libelle1: "Locations",
            value: "7073 - Locations"
        },
        {
            libelle: "7074",
            libelle1: "Boni/reprises, cess. emballages",
            value: "7074 - Boni/reprises, cess. emballages"
        },
        {
            libelle: "7075",
            libelle1: "Mise à disposition de personnel",
            value: "7075 - Mise à disposition de personnel"
        },
        {
            libelle: "7076",
            libelle1: "Redevances brevets, logiciels",
            value: "7076 - Redevances brevets, logiciels"
        },
        {
            libelle: "7077",
            libelle1: "Service dans l'intérêt personnel",
            value: "7077 - Service dans l'intérêt personnel"
        },
        {
            libelle: "7078",
            libelle1: "Autres produits accessoires",
            value: "7078 - Autres produits accessoires"
        },
        {
            libelle: "71",
            libelle1: "Subventions d'exploitation",
            value: "71 - Subventions d'exploitation"
        },
        {
            libelle: "711",
            libelle1: "Sur produits à l'exportation",
            value: "711 - Sur produits à l'exportation"
        },
        {
            libelle: "712",
            libelle1: "Sur produits à l'importation",
            value: "712 - Sur produits à l'importation"
        },
        {
            libelle: "713",
            libelle1: "Sur produits de péréquation",
            value: "713 - Sur produits de péréquation"
        },
        {
            libelle: "718",
            libelle1: "Autres subventions exploitation",
            value: "718 - Autres subventions exploitation"
        },
        {
            libelle: "72",
            libelle1: "Production immobilisée",
            value: "72 - Production immobilisée"
        },
        {
            libelle: "721",
            libelle1: "Immobilisations incorporelles",
            value: "721 - Immobilisations incorporelles"
        },
        {
            libelle: "722",
            libelle1: "Immobilisations corporelles",
            value: "722 - Immobilisations corporelles"
        },
        {
            libelle: "726",
            libelle1: "Immobilisations financières",
            value: "726 - Immobilisations financières"
        },
        {
            libelle: "73",
            libelle1: "Variat. Stocks biens et services",
            value: "73 - Variat. Stocks biens et services"
        },
        {
            libelle: "734",
            libelle1: "Variat. Stocks produits en cours",
            value: "734 - Variat. Stocks produits en cours"
        },
        {
            libelle: "735",
            libelle1: "Variations : en-cours services",
            value: "735 - Variations : en-cours services"
        },
        {
            libelle: "736",
            libelle1: "Variat. : stocks produits finis",
            value: "736 - Variat. : stocks produits finis"
        },
        {
            libelle: "737",
            libelle1: "Variat. stocks produit interméd.",
            value: "737 - Variat. stocks produit interméd."
        },
        {
            libelle: "75",
            libelle1: "Autres produits",
            value: "75 - Autres produits"
        },
        {
            libelle: "752",
            libelle1: "QP résultat / opérat.  en commun",
            value: "752 - QP résultat / opérat.  en commun"
        },
        {
            libelle: "7521",
            libelle1: "Quote-part transférée de pertes",
            value: "7521 - Quote-part transférée de pertes"
        },
        {
            libelle: "7525",
            libelle1: "Bénéfices attribués par transfert",
            value: "7525 - Bénéfices attribués par transfert"
        },
        {
            libelle: "753",
            libelle1: "QP résultat /éxecut.part.contrat",
            value: "753 - QP résultat /éxecut.part.contrat"
        },
        {
            libelle: "754",
            libelle1: "Pdt cessions courantes d'immob.",
            value: "754 - Pdt cessions courantes d'immob."
        },
        {
            libelle: "7541",
            libelle1: "Prix cession Immobilisations incorporelles",
            value: "7541 - Prix cession Immobilisations incorporelles"
        },
        {
            libelle: "7542",
            libelle1: "Prix cession Immobilisations corporelles",
            value: "7542 - Prix cession Immobilisations corporelles"
        },
        {
            libelle: "7546",
            libelle1: "Prix cession Immobilisations financières",
            value: "7546 - Prix cession Immobilisations financières"
        },
        {
            libelle: "758",
            libelle1: "Produits divers",
            value: "758 - Produits divers"
        },
        {
            libelle: "7581",
            libelle1: "Jetons présence et autres-Adm",
            value: "7581 - Jetons présence et autres-Adm"
        },
        {
            libelle: "7582",
            libelle1: "Indemnités d'assurances reçues",
            value: "7582 - Indemnités d'assurances reçues"
        },
        {
            libelle: "759",
            libelle1: "Rep. charge provision. exploitat",
            value: "759 - Rep. charge provision. exploitat"
        },
        {
            libelle: "7591",
            libelle1: "Sur risques à court terme",
            value: "7591 - Sur risques à court terme"
        },
        {
            libelle: "7593",
            libelle1: "Sur stocks",
            value: "7593 - Sur stocks"
        },
        {
            libelle: "7594",
            libelle1: "Sur créances",
            value: "7594 - Sur créances"
        },
        {
            libelle: "7598",
            libelle1: "Sur autres charges provisionnées",
            value: "7598 - Sur autres charges provisionnées"
        },
        {
            libelle: "77",
            libelle1: "Revenus financiers et assimilés",
            value: "77 - Revenus financiers et assimilés"
        },
        {
            libelle: "771",
            libelle1: "Intérêts de prêts",
            value: "771 - Intérêts de prêts"
        },
        {
            libelle: "772",
            libelle1: "Revenus de participations",
            value: "772 - Revenus de participations"
        },
        {
            libelle: "773",
            libelle1: "Escomptes obtenus",
            value: "773 - Escomptes obtenus"
        },
        {
            libelle: "774",
            libelle1: "Revenus de titres de placement",
            value: "774 - Revenus de titres de placement"
        },
        {
            libelle: "776",
            libelle1: "Gains de change",
            value: "776 - Gains de change"
        },
        {
            libelle: "777",
            libelle1: "Gains Cessions titres placement",
            value: "777 - Gains Cessions titres placement"
        },
        {
            libelle: "778",
            libelle1: "Gains sur risques financiers",
            value: "778 - Gains sur risques financiers"
        },
        {
            libelle: "779",
            libelle1: "Rep. charges prov. financières",
            value: "779 - Rep. charges prov. financières"
        },
        {
            libelle: "7791",
            libelle1: "Sur risques financiers",
            value: "7791 - Sur risques financiers"
        },
        {
            libelle: "7795",
            libelle1: "Sur titres de placement",
            value: "7795 - Sur titres de placement"
        },
        {
            libelle: "7798",
            libelle1: "Aut. charges provis. financières",
            value: "7798 - Aut. charges provis. financières"
        },
        {
            libelle: "78",
            libelle1: "Transferts de charges",
            value: "78 - Transferts de charges"
        },
        {
            libelle: "781",
            libelle1: "Transferts charges exploitation",
            value: "781 - Transferts charges exploitation"
        },
        {
            libelle: "787",
            libelle1: "Transferts charges financières",
            value: "787 - Transferts charges financières"
        },
        {
            libelle: "79",
            libelle1: "Reprises de provisions",
            value: "79 - Reprises de provisions"
        },
        {
            libelle: "791",
            libelle1: "Reprises provisions exploitat.",
            value: "791 - Reprises provisions exploitat."
        },
        {
            libelle: "7911",
            libelle1: "Pour risques et charges",
            value: "7911 - Pour risques et charges"
        },
        {
            libelle: "7912",
            libelle1: "Pour grosses réparations",
            value: "7912 - Pour grosses réparations"
        },
        {
            libelle: "7913",
            libelle1: "dépréciat. : immob. incorporel.",
            value: "7913 - dépréciat. : immob. incorporel."
        },
        {
            libelle: "7914",
            libelle1: "Dépréciat. : immob. corporelles",
            value: "7914 - Dépréciat. : immob. corporelles"
        },
        {
            libelle: "797",
            libelle1: "Reprises provisions financières",
            value: "797 - Reprises provisions financières"
        },
        {
            libelle: "7971",
            libelle1: "Pour risques et charges",
            value: "7971 - Pour risques et charges"
        },
        {
            libelle: "7972",
            libelle1: "Dépréciat. : immob. financières",
            value: "7972 - Dépréciat. : immob. financières"
        },
        {
            libelle: "7978",
            libelle1: "Reprises d'amortissements",
            value: "7978 - Reprises d'amortissements"
        },
        {
            libelle: "8",
            libelle1: "Comptes des autres charges et autres produits",
            value: "8 - Comptes des autres charges et autres produits"
        },
        {
            libelle: "81",
            libelle1: "Valeurs comptables cess. immob.",
            value: "81 - Valeurs comptables cess. immob."
        },
        {
            libelle: "8111",
            libelle1: "Val.Brute Immobilisations incorporelles",
            value: "8111 - Val.Brute Immobilisations incorporelles"
        },
        {
            libelle: "8118",
            libelle1: "Amort. Immobilisations incorporelles",
            value: "8118 - Amort. Immobilisations incorporelles"
        },
        {
            libelle: "8121",
            libelle1: "Val.Brute Immobilisations corporelles",
            value: "8121 - Val.Brute Immobilisations corporelles"
        },
        {
            libelle: "8128",
            libelle1: "Amort. Immobilisations corporelles",
            value: "8128 - Amort. Immobilisations corporelles"
        },
        {
            libelle: "8161",
            libelle1: "Val.Brute Immobilisations financières",
            value: "8161 - Val.Brute Immobilisations financières"
        },
        {
            libelle: "8168",
            libelle1: "Amort. Immobilisations financières",
            value: "8168 - Amort. Immobilisations financières"
        },
        {
            libelle: "82",
            libelle1: "Produits des cess. immobilisat.",
            value: "82 - Produits des cess. immobilisat."
        },
        {
            libelle: "821",
            libelle1: "Prix cession Immobilisations incorporelles",
            value: "821 - Prix cession Immobilisations incorporelles"
        },
        {
            libelle: "822",
            libelle1: "Prix cession Immobilisations corporelles",
            value: "822 - Prix cession Immobilisations corporelles"
        },
        {
            libelle: "826",
            libelle1: "Prix cession Immobilisations financières",
            value: "826 - Prix cession Immobilisations financières"
        },
        {
            libelle: "83",
            libelle1: "Charges hors activité ordinaire",
            value: "83 - Charges hors activité ordinaire"
        },
        {
            libelle: "831",
            libelle1: "Charges H.A.O. constatées",
            value: "831 - Charges H.A.O. constatées"
        },
        {
            libelle: "834",
            libelle1: "Pertes sur créances H.A.O.",
            value: "834 - Pertes sur créances H.A.O."
        },
        {
            libelle: "835",
            libelle1: "Dons et libéralités accordés",
            value: "835 - Dons et libéralités accordés"
        },
        {
            libelle: "836",
            libelle1: "Abandons de créances consentis",
            value: "836 - Abandons de créances consentis"
        },
        {
            libelle: "839",
            libelle1: "Charges provisionnées H.A.O.",
            value: "839 - Charges provisionnées H.A.O."
        },
        {
            libelle: "8393",
            libelle1: "Charges provisionnées H.A.O. Stocks",
            value: "8393 - Charges provisionnées H.A.O. Stocks"
        },
        {
            libelle: "8394",
            libelle1: "Charges provisionnées H.A.O. Tiers",
            value: "8394 - Charges provisionnées H.A.O. Tiers"
        },
        {
            libelle: "8395",
            libelle1: "Charges provisionnées H.A.O. Trésorerie",
            value: "8395 - Charges provisionnées H.A.O. Trésorerie"
        },
        {
            libelle: "84",
            libelle1: "Produits hors activité ordinaire",
            value: "84 - Produits hors activité ordinaire"
        },
        {
            libelle: "841",
            libelle1: "Produits H.A.O. constatés",
            value: "841 - Produits H.A.O. constatés"
        },
        {
            libelle: "845",
            libelle1: "Dons et libéralités obtenus",
            value: "845 - Dons et libéralités obtenus"
        },
        {
            libelle: "846",
            libelle1: "Abandons de créances obtenus",
            value: "846 - Abandons de créances obtenus"
        },
        {
            libelle: "848",
            libelle1: "Transferts de charges H.A.O.",
            value: "848 - Transferts de charges H.A.O."
        },
        {
            libelle: "849",
            libelle1: "Reprises sur Charges provisionnées H.A.O.",
            value: "849 - Reprises sur Charges provisionnées H.A.O."
        },
        {
            libelle: "8493",
            libelle1: "Rep. Charges provisionnées H.A.O. Stocks",
            value: "8493 - Rep. Charges provisionnées H.A.O. Stocks"
        },
        {
            libelle: "8494",
            libelle1: "Rep. Charges provisionnées H.A.O. Tiers",
            value: "8494 - Rep. Charges provisionnées H.A.O. Tiers"
        },
        {
            libelle: "8495",
            libelle1: "Rep. Charges provisionnées H.A.O. Trésorerie",
            value: "8495 - Rep. Charges provisionnées H.A.O. Trésorerie"
        },
        {
            libelle: "85",
            libelle1: "Dotat. hors activité ordinaire",
            value: "85 - Dotat. hors activité ordinaire"
        },
        {
            libelle: "851",
            libelle1: "Dotat. aux provis. réglementées",
            value: "851 - Dotat. aux provis. réglementées"
        },
        {
            libelle: "852",
            libelle1: "Dotat. aux amortissem. H.A.O.",
            value: "852 - Dotat. aux amortissem. H.A.O."
        },
        {
            libelle: "853",
            libelle1: "Dotat. provis. dépréciat. H.A.O.",
            value: "853 - Dotat. provis. dépréciat. H.A.O."
        },
        {
            libelle: "854",
            libelle1: "Dotat. provis. R & C H.A.O.",
            value: "854 - Dotat. provis. R & C H.A.O."
        },
        {
            libelle: "858",
            libelle1: "Autres dotations H.A.O.",
            value: "858 - Autres dotations H.A.O."
        },
        {
            libelle: "86",
            libelle1: "Reprises hors activité ordinaire",
            value: "86 - Reprises hors activité ordinaire"
        },
        {
            libelle: "861",
            libelle1: "Reprises provisions réglementées",
            value: "861 - Reprises provisions réglementées"
        },
        {
            libelle: "862",
            libelle1: "Reprises d'amortissements H.A.O.",
            value: "862 - Reprises d'amortissements H.A.O."
        },
        {
            libelle: "863",
            libelle1: "Repris. provis. dépréc. H.A.O.",
            value: "863 - Repris. provis. dépréc. H.A.O."
        },
        {
            libelle: "864",
            libelle1: "Rep. provis. R & C H.A.O.",
            value: "864 - Rep. provis. R & C H.A.O."
        },
        {
            libelle: "865",
            libelle1: "Rep. subvent. investissement",
            value: "865 - Rep. subvent. investissement"
        },
        {
            libelle: "868",
            libelle1: "Autres Reprises H.A.O.",
            value: "868 - Autres Reprises H.A.O."
        },
        {
            libelle: "87",
            libelle1: "Participation des travailleurs",
            value: "87 - Participation des travailleurs"
        },
        {
            libelle: "88",
            libelle1: "Subventions d'équilibre",
            value: "88 - Subventions d'équilibre"
        },
        {
            libelle: "89",
            libelle1: "Impôts sur le résultat",
            value: "89 - Impôts sur le résultat"
        },
        {
            libelle: "891",
            libelle1: "Impôts bénéfices (exercice)",
            value: "891 - Impôts bénéfices (exercice)"
        },
        {
            libelle: "892",
            libelle1: "Rappels impôts / résultat antér.",
            value: "892 - Rappels impôts / résultat antér."
        },
        {
            libelle: "895",
            libelle1: "Impôt minimum forfaitaire I.M.F.",
            value: "895 - Impôt minimum forfaitaire I.M.F."
        },
        {
            libelle: "899",
            libelle1: "Dégrèvem. impôts / résult. ant.",
            value: "899 - Dégrèvem. impôts / résult. ant."
        },
        {
            libelle: "9",
            libelle1: "Comptes des engagements ",
            value: "9 - Comptes des engagements "
        },
        {
            libelle: "901",
            libelle1: "Engagements de financement obtenus",
            value: "901 - Engagements de financement obtenus"
        },
        {
            libelle: "9011",
            libelle1: "Crédits confirmés obtenus",
            value: "9011 - Crédits confirmés obtenus"
        },
        {
            libelle: "9012",
            libelle1: "Emprunts restant à encaisser",
            value: "9012 - Emprunts restant à encaisser"
        },
        {
            libelle: "9013",
            libelle1: "Facilités financières renouvelables",
            value: "9013 - Facilités financières renouvelables"
        },
        {
            libelle: "9014",
            libelle1: "Facilités d'émission",
            value: "9014 - Facilités d'émission"
        },
        {
            libelle: "9018",
            libelle1: "Autres engagements de financement obtenus",
            value: "9018 - Autres engagements de financement obtenus"
        },
        {
            libelle: "902",
            libelle1: "Engagements de garantie obtenus",
            value: "902 - Engagements de garantie obtenus"
        },
        {
            libelle: "9021",
            libelle1: "Avals obtenus",
            value: "9021 - Avals obtenus"
        },
        {
            libelle: "9022",
            libelle1: "Cautions, garanties obtenues",
            value: "9022 - Cautions, garanties obtenues"
        },
        {
            libelle: "9023",
            libelle1: "Hypothèques obtenues",
            value: "9023 - Hypothèques obtenues"
        },
        {
            libelle: "9024",
            libelle1: "Effets endossés par des tiers",
            value: "9024 - Effets endossés par des tiers"
        },
        {
            libelle: "9028",
            libelle1: "Autres garanties obtenues",
            value: "9028 - Autres garanties obtenues"
        },
        {
            libelle: "903",
            libelle1: "Engagements réciproques",
            value: "903 - Engagements réciproques"
        },
        {
            libelle: "9031",
            libelle1: "Achats de marchandises à terme",
            value: "9031 - Achats de marchandises à terme"
        },
        {
            libelle: "9032",
            libelle1: "Achats à terme de devises",
            value: "9032 - Achats à terme de devises"
        },
        {
            libelle: "9033",
            libelle1: "Commandes fermes des clients",
            value: "9033 - Commandes fermes des clients"
        },
        {
            libelle: "9038",
            libelle1: "Autres engagements réciproques",
            value: "9038 - Autres engagements réciproques"
        },
        {
            libelle: "904",
            libelle1: "Autres engagements obtenus",
            value: "904 - Autres engagements obtenus"
        },
        {
            libelle: "9041",
            libelle1: "Abandons créances conditionnels",
            value: "9041 - Abandons créances conditionnels"
        },
        {
            libelle: "9043",
            libelle1: "Ventes clause réserve propriété",
            value: "9043 - Ventes clause réserve propriété"
        },
        {
            libelle: "9048",
            libelle1: "Divers engagements obtenus",
            value: "9048 - Divers engagements obtenus"
        },
        {
            libelle: "905",
            libelle1: "Engagements de financement accordés",
            value: "905 - Engagements de financement accordés"
        },
        {
            libelle: "9051",
            libelle1: "Crédits accordés non encaissés",
            value: "9051 - Crédits accordés non encaissés"
        },
        {
            libelle: "9058",
            libelle1: "Autres engagements de financement accordés",
            value: "9058 - Autres engagements de financement accordés"
        },
        {
            libelle: "906",
            libelle1: "Engagements de garantie accordés",
            value: "906 - Engagements de garantie accordés"
        },
        {
            libelle: "9061",
            libelle1: "Avals accordés",
            value: "9061 - Avals accordés"
        },
        {
            libelle: "9062",
            libelle1: "Cautions, garanties accordées",
            value: "9062 - Cautions, garanties accordées"
        },
        {
            libelle: "9063",
            libelle1: "Hypothèques accordées",
            value: "9063 - Hypothèques accordées"
        },
        {
            libelle: "9064",
            libelle1: "Effets endossés par l'entreprise",
            value: "9064 - Effets endossés par l'entreprise"
        },
        {
            libelle: "9068",
            libelle1: "Autres garanties accordées",
            value: "9068 - Autres garanties accordées"
        },
        {
            libelle: "907",
            libelle1: "Engagements réciproques",
            value: "907 - Engagements réciproques"
        },
        {
            libelle: "9071",
            libelle1: "Ventes de marchandises à terme",
            value: "9071 - Ventes de marchandises à terme"
        },
        {
            libelle: "9072",
            libelle1: "Ventes à terme de devises",
            value: "9072 - Ventes à terme de devises"
        },
        {
            libelle: "9073",
            libelle1: "Commandes fermes aux fournisseur",
            value: "9073 - Commandes fermes aux fournisseur"
        },
        {
            libelle: "9078",
            libelle1: "Autres engagements réciproques",
            value: "9078 - Autres engagements réciproques"
        },
        {
            libelle: "908",
            libelle1: "Autres engagements accordés",
            value: "908 - Autres engagements accordés"
        },
        {
            libelle: "9081",
            libelle1: "Annulations conditionelles de dettes",
            value: "9081 - Annulations conditionelles de dettes"
        },
        {
            libelle: "9082",
            libelle1: "Engagements de retraite",
            value: "9082 - Engagements de retraite"
        },
        {
            libelle: "9083",
            libelle1: "Achats clause réserve propriété",
            value: "9083 - Achats clause réserve propriété"
        },
        {
            libelle: "9088",
            libelle1: "Divers engagements accordés",
            value: "9088 - Divers engagements accordés"
        }
    ]
;
