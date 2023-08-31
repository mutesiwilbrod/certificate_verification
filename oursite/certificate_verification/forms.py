from django import forms
from . models import Certificate

class VerificationForm(forms.Form):
    certificate_number = forms.CharField(label='Certificate Number', max_length=100)
    recipient_name = forms.CharField(label='recipient_name', max_length=100)
    issue_date = forms.DateField(label='issue_date')

