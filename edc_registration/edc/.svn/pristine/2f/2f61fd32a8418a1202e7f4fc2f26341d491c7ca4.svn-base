from django import forms

from edc.register.models import TITLE_CHOICES

FIELD_SIZE = 40 

class UserForm(forms.Form):

   title = forms.CharField(widget=forms.Select(choices=TITLE_CHOICES))

   lastName  = forms.CharField(widget=forms.TextInput(attrs={'size': FIELD_SIZE,}), label='Last name')
   firstName = forms.CharField(widget=forms.TextInput(attrs={'size': FIELD_SIZE,}), label = 'First name')
   emailaddress = forms.EmailField(widget=forms.TextInput(attrs={'size': FIELD_SIZE,}), label='E-mail address')
   department = forms.CharField(widget=forms.TextInput(attrs={'size': FIELD_SIZE,}), label = 'Group/department', required=True)
   institute  = forms.CharField(widget=forms.TextInput(attrs={'size': FIELD_SIZE,}), label='Institution/compay name', required=True)
   dataUse    = forms.CharField(label='Proposed use of data', required=True, widget=forms.Textarea(attrs={'cols':80,'rows':5}))
   acceptConditions = forms.BooleanField(widget=forms.CheckboxInput(), required=True)

class ConditionForm(forms.ModelForm):

   text = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows':'25', 'cols': '100'}))
