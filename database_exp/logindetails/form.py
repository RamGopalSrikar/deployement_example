from django import forms
from logindetails.models import userlogin
class FormName(forms.ModelForm):
    class Meta:
        model=userlogin
        fields='__all__'
        
