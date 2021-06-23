from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(help_text="enter your query!")
    
