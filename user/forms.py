from django.contrib.auth.forms import UserCreationForm
from user.models import User
from django import forms
from django.contrib.auth import authenticate


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

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError('first_name must be alphabet')
        return first_name
            
    def clean_last_name(self): 
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise forms.ValidationError('last_name must be alphabet')
        return last_name


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
        
    def clean(self):
        print("\33[32;1mclean function called\33[0m")
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")