from django import forms

class SearchForm(forms.Form):
    string = forms.CharField(max_length=160)