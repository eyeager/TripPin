from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
 #  url(r'^$', views.index, name='index'),
 url(r'^signup/$', views.signup, name = 'signup'),
 url(r'^login/$', views.login, name = 'login'),
 url(r'^register/$', views.register, name='register'),
 url(r'^login_user/$', views.login_user, name='login_user'),
 # url(r'^profile/$', views.profile, name='profile'),
 # url(r'^logout/$', views.logout, name='logout'),
 ]


