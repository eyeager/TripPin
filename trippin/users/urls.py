from django.conf.urls import url
from . import views


urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^signup/$', views.signup, name = 'signup'),
 url(r'^login/$', views.login_page, name = 'login_page'),
 url(r'^register/$', views.register, name='register'),
 url(r'^login_user/$', views.login_user, name='login_user'),
 url(r'^profile/$', views.profile, name='profile'),
 url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
 url(r'^save_profile/$', views.save_profile, name='save_profile'),
 url(r'^change_password/$', views.change_password, name='change_password'),
 url(r'^logout/$', views.logout_user, name='logout_user'),

 # url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : 'password/reset/done/','template_name' :'users/reset_password.html'},name="password_reset"),
 # url(r'^password/reset/done/$','django.contrib.auth.views.password_reset_done'),
 # url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : 'password/done/'}),
 # url(r'^password/done/$', 'django.contrib.auth.views.password_reset_complete'),
 ]