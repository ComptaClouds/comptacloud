# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from comptacloud import settings
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.contrib.auth.models import Group



class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern

    name = models.CharField(blank=True, max_length=255)
    secondname = models.CharField(blank=True, max_length=255)
    image = models.FileField(upload_to='documents/')
    email_confirmed = models.BooleanField(default=False)
    standard = models.BooleanField(default=True)
    valide = models.BooleanField(default=False)
    autorise = models.BooleanField(default=False)
    relations = models.ManyToManyField('self',
                                       symmetrical=False)


    class Meta:
        permissions = (
            ("can_see_dealer_price", "Can see dealer price"),
        )

        def __str__(self):
            return self.email

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
class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.entreprise, filename)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documents', on_delete=models.CASCADE, default=1)
    entreprise = models.CharField(max_length=255, default='merde')


class Fournisseurs(models.Model):
    nom = models.CharField(max_length=45, blank=True, null=True)

class liaison(models.Model):
   entrepriseid =  models.CharField(max_length=255, default='merde')
   comptableid =  models.CharField(max_length=255, default='merde')


class operationcompta(models.Model):
    useridsaisie = models.IntegerField(null=True)
    useridimputer = models.IntegerField(null=True)
    typejournal_idtypejournal = models.PositiveIntegerField()
    libelle = models.CharField(max_length=45, blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    prixunitaire = models.FloatField(blank=True, null=True)
    dateoperation = models.DateField(blank=True, null=True)
    datesaisie = models.DateField(blank=True, null=True)
    dateimput = models.DateField(blank=True, null=True)
    reference = models.CharField(max_length=45, blank=True, null=True)
    quantité = models.IntegerField(null=True)
    fournisseurs = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,related_name='+')
    entrepriseid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,related_name='+')

    def __str__(self):
        return self.libelle



class Compte(models.Model):
    compteid = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45, blank=True, null=True)
    classe = models.IntegerField(blank=True, null=True)


class Credit(models.Model):
    idcredit = models.AutoField(primary_key=True)
    operationid = models.ForeignKey(operationcompta, on_delete=models.CASCADE, null=True)
    compte_compteid = models.IntegerField(blank=True, null=True)
    operation_user_2_useridsaisie = models.IntegerField(blank=True, null=True)
    operation_user_2_useridimputer = models.IntegerField(blank=True, null=True)
    operation_typejournal_idtypejournal = models.PositiveIntegerField(blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)


class Debit(models.Model):
    iddebit = models.AutoField(primary_key=True)
    operationid = models.ForeignKey(operationcompta, on_delete=models.CASCADE, null=True)
    compte_compteid = models.IntegerField(blank=True, null=True)
    operation_user_2_useridsaisie = models.IntegerField(blank=True, null=True)
    operation_user_2_useridimputer = models.IntegerField(blank=True, null=True)
    operation_typejournal_idtypejournal = models.PositiveIntegerField(blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)

class Typejournal(models.Model):
    idtypejournal = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=45, blank=True, null=True)
