from django.conf.urls import url
from django.urls import path
from . import views


#urlpatterns = [
   # url(r'^$', views.voiruser2, name='voiruser2'),
   # url(r'^creeruser/(?P<pk>[0-9]+)/$', views.voiruser, name='voiruser'),
   # url(r'^creeruser/$', views.creeruser, name='creeruser'),
    #url(r'^main/$', views.main, name='login'),
   # url(r'^login/$', views.login_user,name='login'),

#]

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]