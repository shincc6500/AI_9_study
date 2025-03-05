from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import User  

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username',
                  "email",
                "first_name",
                "last_name",]
        
class AssingForm(forms.Form):
    title = forms.CharField(max_length=20)
    content = forms.CharField()

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )
    
    def __init__(self, *args, **kwargs): #링크를 패스워드 변경으로 오버라이딩. 
        super().__init__(*args, **kwargs)
        if self.fields.get("password"):
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(reverse('users:change_passward'))
            self.fields["password"].help_text = password_help_text




class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 
                  'last_name', 
                  'email', 
                  'profile_image', 
                  'bio']