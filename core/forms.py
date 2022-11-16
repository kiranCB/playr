from django import forms
from django import forms
from core import models

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.FeedbackModel
       
        exclude = ('status', )