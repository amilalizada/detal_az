from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm,PasswordResetForm,\
SetPasswordForm
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html

User = get_user_model()


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'user-form-input',
                                          'placeholder': 'Password'
                                          }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'user-form-input',
                                          'placeholder': 'Confirm Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'password1',
            'password2',
            'phone',
        )

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'user-form-input',
                'placeholder': 'Email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'user-form-input',
                'placeholder': 'First name'
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'user-form-input',
                'placeholder': 'Phone'
            }),
        }

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('password and confirm password is not same')
        return super().clean()



class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=40, widget=forms.EmailInput(attrs={
        'class': 'login-input',
        'placeholder': 'Email'
    }))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
        'class': 'login-input',
        'placeholder': 'Password'
    }))
    
    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 
        'autofocus': True,
        'class': 'user-form-input',
        'placeholder': 'Old Password',
        }),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
        'class': 'user-form-input',
        'placeholder': 'New Password',
            }),
    )
    new_password2 = forms.CharField(
        label=_("Confirm New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
        'class': 'user-form-input',
        'placeholder': 'Confirm New Password',
        }),
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'user-form-input',
            'placeholder': _('Email'),
        })
    )


class ResetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
        'class': 'user-form-input',
        'placeholder': 'New Password',}),
        strip=False,
        help_text=password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
        'class': 'user-form-input',
        'placeholder': 'New password confirmation',}),
    )

