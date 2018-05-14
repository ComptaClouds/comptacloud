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
    path('model_form_upload/', views.model_form_upload, name='model_form_upload'),
    path('autorise/', views.autorise, name='autorise'),
    path('enregistrement/', views.enregistrement, name='enregistrement'),
    url(r'account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),



]