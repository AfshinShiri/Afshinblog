from django import forms
from . import models
class commentsform(forms.ModelForm):
    class Meta:
        model = models.comments
        fields = ['name','email','body']
