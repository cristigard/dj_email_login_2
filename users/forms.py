from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, 
                                        PasswordChangeForm, PasswordResetForm)





class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username','password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; ',
                }),
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 300px;'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width: 300px;'})
        
        

class CutomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [ 'email', 'username']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; ',
                }),
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            }



#manage widget of form in PasswordReset
class CustomUserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update(
            {'class': "form-control",
                        'style': 'max-width: 300px;'}
            )


#manage widget of form in PasswordChange
class CustomUserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update(
            {'class': "form-control",
                        'style': 'max-width: 300px;'}
            )
        self.fields['new_password1'].widget.attrs.update(
            {'class': "form-control",
                        'style': 'max-width: 300px;'}
            )
        self.fields['new_password2'].widget.attrs.update(
            {'class': "form-control",
                        'style': 'max-width: 300px;'}
            )


#manage widget of form in LoginView
class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'class': "form-control",
                    'style': 'max-width: 300px;'}
        )
        self.fields['password'].widget.attrs.update(
        {'class': "form-control",
                    'style': 'max-width: 300px;'}
        )
        self.fields['username'].label = 'Email / Username'
        
        
