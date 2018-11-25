#  * This file is part of Tripple A Express project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm


from accounts.models import CustomUser

# These User creation form will be use by staff users


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields

# These User creation form will be use by staff users


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'Username or e-mail',
                'autofocus': 'autofocus'
            }
        )

        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'Password',
            }
        )


class CustomSignupForm(SignupForm):

    phone_number = forms.CharField( max_length=15, required=True)


    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'E-mail address',
                'autofocus': 'autofocus'
            }
        )

        self.fields['phone_number'].widget = forms.TextInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'Phone Number'
            }
        )

        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'Password'
            }
        )

        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'Password (again)'
            }
        )

    def save(self, request):
        # call the parent classes save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user

class CustomResetPasswordForm(ResetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(
            attrs={
                'class': 'form__input',
                'placeholder': 'E-mail address'
            }
        )
