from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Hike


class HikeForm(ModelForm):
    class Meta:
        model = Hike
        fields = '__all__'
        
class RegisterForm(UserCreationForm): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({ 
            'required': '',
            'name' : 'username' , 
            'id' : 'username' , 
            'type' : 'text' ,
            'class' : 'form-input' , 
            'placeholder' : 'Username' , 
            'maxlength' : '16' , 
            'minlength' : '6'
        })
        self.fields["password1"].widget.attrs.update({ 
            'required': '',
            'name' : 'password1' , 
            'id' : 'password1' , 
            'type' : 'password' , 
            'placeholder' : 'password' , 
            'maxlength' : '22' , 
            'minlength' : '8'
        })
        self.fields["password2"].widget.attrs.update({ 
            'required' : '',
            'name' : 'password2' , 
            'id' : 'password2' , 
            'type' : 'password' ,
            'placeholder' : 'password' , 
            'maxlength' : '22' , 
            'minlength' : '8'
        })
        
    class Meta: 
        model = User 
        fields = ('username' , 'password1' , 'password2') 
