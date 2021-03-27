from django import forms
from .models import ScoreCreate
from django.forms import SelectDateWidget
from .choices import sport_choices

class ScoreForm(forms.ModelForm):
    class Meta:
        model = ScoreCreate
        fields = ['title','slug', 'sport', 'home','away','date', 'startTime']
        labels = {
            'startTime': 'Start Time'
        }
        widgets = {
            'date': SelectDateWidget(empty_label=("Year", "Month", "Date")),
        }

class SelectSportForm(forms.Form):
    choice = forms.ChoiceField(choices=sport_choices)

class ScoreUpdateForm(forms.ModelForm):
    class Meta:
        model = ScoreCreate
        fields = ['homeScore', 'awayScore']
        
