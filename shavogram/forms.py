from django import forms
from .models import Photo,Profile

class PictureForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['user','pub_date','likes']

class ProfileForm(forms.Form):
    bio = forms.CharField(label = "Bio")
    picture = forms.ImageField(label = "Picture") 
