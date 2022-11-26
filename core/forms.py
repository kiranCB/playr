from django import forms
from django import forms
from core import models

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.FeedbackModel
       
        exclude = ('status', )

class HostForm(forms.ModelForm):
    class Meta:
        model = models.HostModel

        exclude = ('status','created_on','updated_on')

class JoinForm(forms.ModelForm):
    class Meta:
        model = models.JoinModel

        exclude = ('status','created_on','updated_on')
