from django.forms import ModelForm
from .models import Room


class HikeForm(ModelForm):
    class Meta:
        model = HikeForm
        fields = '__all__'
