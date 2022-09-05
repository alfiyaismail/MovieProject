from django import forms
from . models import Movie

'''form of movie model for updation'''
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','year','img']


