# we gonna create django form for regiser page
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm




class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-2 border-right-0 border'}))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=({'class':'form-control py-2 border-right-0 border'})))
    password = forms.CharField(widget=forms.PasswordInput(attrs=({'class': 'form-control py-2 border-right-0 border'})))

class RegistrationForm(UserCreationForm):
#UserCreationForm
# A form that creates a user, with no privileges, from the given username and password.
    email = forms.EmailField(required = True, widget=forms.EmailInput(
        attrs=({'class': 'form-control py-2 border-right-0 border'})))
    # make e-mail a required UserAttributeSimilarityValidator
    username = forms.CharField(max_length=16, help_text='16 characters max. Letters, digits and @/./+/-/_ only', widget=forms.TextInput(
        attrs=({'class': 'form-control py-2 border-right-0 border'})))
    first_name = forms.CharField(widget=forms.TextInput(attrs=({'class': 'form-control py-2 border-right-0 border'})))
    last_name = forms.CharField(widget=forms.TextInput(attrs=({'class': 'form-control py-2 border-right-0 border'})))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=({'class': 'form-control py-2 border-right-0 border'})))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=({'class': 'form-control py-2 border-right-0 border'})))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
    def save(self, commit = True):
        #prevents user from entering sql or harmful data
        user = super(RegistrationForm, self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    username = forms.CharField(max_length = 16, help_text='16 characters max. Letters, digits and @/./+/-/_ only')
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        )

class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control py-2 border-right-0 border'}))
    new_password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control py-2 border-right-0 border'}))
    new_password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control py-2 border-right-0 border'}))