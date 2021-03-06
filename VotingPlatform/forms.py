from django import forms
from models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ('votes_first_round', 'votes_second_round', 'round', )
        widgets = {'picture' : forms.FileInput() }

class CandidateEditForm(forms.ModelForm):
    class Meta:
        model = Candidate
        widgets = {'picture' : forms.FileInput() }
