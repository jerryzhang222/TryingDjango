from django import forms
from .models import Join

class EmailForm(forms.Form):
    email = forms.EmailField()
    file = forms.FileField()
    
class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = '__all__'