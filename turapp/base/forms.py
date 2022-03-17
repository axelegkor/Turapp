from django import forms
from django.forms import ModelForm

from .models import Hike


class HikeForm(ModelForm):
    class Meta:
        model = Hike
        fields = '__all__'
