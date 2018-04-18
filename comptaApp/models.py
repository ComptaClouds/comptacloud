# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)
    secondname = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email


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


class Operation(models.Model):
    operationid = models.AutoField(primary_key=True)
    user_2_useridsaisie = models.IntegerField()
    user_2_useridimputer = models.IntegerField()
    typejournal_idtypejournal = models.PositiveIntegerField()
    libelle = models.CharField(max_length=45, blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    dateoperation = models.DateField(blank=True, null=True)
    datesaisie = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operation'
        unique_together = (('operationid', 'user_2_useridsaisie', 'user_2_useridimputer', 'typejournal_idtypejournal'),)


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