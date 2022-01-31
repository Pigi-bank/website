from django import forms

class SubscribeForm(forms.Form):
  name= forms.CharField(max_length=50)
  phone_number = forms.IntegerField(label='Mobile Number')
  email = forms.EmailField(label='Email')