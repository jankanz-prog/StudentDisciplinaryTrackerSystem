from django import forms
from .models import DisciplinaryIncident, Sanction


class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = DisciplinaryIncident
        fields = ['student', 'description', 'severity_level', 'reported_by']


class SanctionForm(forms.ModelForm):
    class Meta:
        model = Sanction
        fields = ['incident', 'student', 'description', 'duration', 'severity_level', 'issued_by']
