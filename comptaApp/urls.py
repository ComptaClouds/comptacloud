from django.conf.urls import url
from django.urls import path
from . import views
from django.urls import path, include


#urlpatterns = [
   # url(r'^$', views.voiruser2, name='voiruser2'),
   # url(r'^creeruser/(?P<pk>[0-9]+)/$', views.voiruser, name='voiruser'),
   # url(r'^creeruser/$', views.creeruser, name='creeruser'),
    #url(r'^main/$', views.main, name='login'),
   # url(r'^login/$', views.login_user,name='login'),

#]

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('modifier/', views.modifier, name='modifier'),


    path('modifierimputation/(?P<pk>[0-9]+)/$', views.modifierimputation, name='modifierimputation'),
    path('model_form_upload/', views.model_form_upload, name='model_form_upload'),
    path('autorise/', views.autorise, name='autorise'),
    path('liaisons/', views.liaisons, name='liaisons'),
    path('listeoperationsimputees/', views.listeoperationsimputees, name='listeoperationsimputees'),
    path('saisiesoperations/', views.saisiesoperations, name='saisiesoperations'),
    path('enregistrement/', views.enregistrement, name='enregistrement'),
    path('paiementdeclaration/', views.paiement, name='paiementdeclaration'),
    path('imputation/', views.imputationss, name='imputation'),
    path('fourni/', views.fourni, name='fourni'),
    path('scan/', views.scan, name='scan'),
    path('declaration/', views.declarations, name='declaration'),
    path('journalcentral/', views.journal_central, name='journalcentral'),
    path('afficherfournisseurs/', views.afficherfournisseurs, name='afficherfournisseurs'),
    url(r'account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),




]