from django import forms

class CreateTicket(forms.Form):
    subject = forms.CharField()
    account = forms.CharField()
    
class AddEntry(forms.Form):
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)