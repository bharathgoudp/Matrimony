
from django import forms
from matriapp.models import Matridata
class matriForm(forms.ModelForm):
    class Meta:
        model =Matridata
        fields = "__all__"

