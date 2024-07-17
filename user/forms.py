from django.contrib.auth.forms import UserCreationForm
from user.models import User
from django import forms

class RegisterationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='required. Add a valid email')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')
        
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username "{username}" is already in use.')