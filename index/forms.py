from django import forms

class Courses(forms.Form):
    checkbox = forms.BooleanField(label='')
