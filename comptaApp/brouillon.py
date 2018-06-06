


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


