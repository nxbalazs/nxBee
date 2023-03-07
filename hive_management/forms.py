from django import forms
from hive_management.models import Hive, Inspection, Treatment

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

class AddInspectionForm(forms.ModelForm):
    queen = forms.BooleanField(initial=True, required=False)
    eggs = forms.BooleanField(initial=True, required=False)
    open_brood = forms.BooleanField(initial=True, required=False)
    sealed_brood = forms.BooleanField(initial=True, required=False)
    class Meta:
        model = Inspection
        fields = '__all__'
        exclude = ('hive',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inspection title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'honey': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Honey'}),
            'varroa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Varroa'}),
            'created_on': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}),
        }

class AddTreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'
        exclude = ('hive',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Treatment Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'med_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicine Name'}),
            'created_on': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}),
        }
