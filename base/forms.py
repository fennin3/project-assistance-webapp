from django import forms
from .models import Message, Testimony


class MessageForm(forms.ModelForm):
    message = forms.Textarea()
    class Meta:
        model=Message
        fields= ['first_name','last_name','email','tel_number','message']

class TestimonyForm(forms.ModelForm):
    feedback = forms.Textarea()
    class Meta:
        model = Testimony
        fields = ['fullname', 'email', 'feedback']