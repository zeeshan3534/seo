from django import forms

class TrafficChecker(forms.Form):
    data = forms.CharField( max_length=80)
