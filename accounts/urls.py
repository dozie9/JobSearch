from django.conf.urls import url
from django.urls import reverse_lazy
from . import views # . looks at all the files within the same level folder
from .forms import LoginForm, CustomPasswordResetForm, PasswordChange
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
PasswordChangeView,
PasswordResetView,
PasswordResetDoneView,
PasswordResetConfirmView,
PasswordResetCompleteView
) # will send e-mail
#passwordResetView sends e-mail

from home.views import HomeView


app_name='accounts'
urlpatterns = [
#subject_template_name='password_reset_subject.txt',success_url='/accounts/password_reset_done/',from_email='support@yoursite.ma'
    url(r'^$', HomeView.as_view(), name='home'), # you can put anything between the ^ and $ for ex: home
    url(r'^login/$', auth_views.LoginView.as_view(template_name = 'accounts/login.html', authentication_form=LoginForm), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name = 'accounts/logout.html'), name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
    url(r'^profile/change-password/$', PasswordChangeView.as_view(template_name="accounts/change_password.html", form_class=PasswordChange, success_url=reverse_lazy('accounts:view_profile')), name='change_password'),
    #url(r'^profile/change-password/$', views.change_password, name='change_password'),

    url(r'^reset-password/$', PasswordResetView.as_view(template_name = 'accounts/reset_password.html', success_url=reverse_lazy('accounts:password_reset_done'), form_class=CustomPasswordResetForm, email_template_name ='accounts/reset_password_email.html'), name='reset_password'),



    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(template_name ='accounts/reset_password_done.html'), name='password_reset_done'),
    #<uidb64>/<token>/
    #
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name ='accounts/reset_password_confirm.html',success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),

    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(template_name = 'accounts/reset_password_complete.html'), name='password_reset_complete'),


]
