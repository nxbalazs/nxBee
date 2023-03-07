from django import forms
from hive_management.models import Hive, Note

class AddHiveForm(forms.ModelForm):
    class Meta:
        model = Hive
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hive Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'supers': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'frames': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control', 'placeholder': '#000000'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Purpose'}),
            'strength': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '90', 'max_value': '100'}),
            'created_on': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}),
        }

class NoteForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note title'}))
    body = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a note'}))
