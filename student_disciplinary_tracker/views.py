from django.shortcuts import render, redirect
from django.contrib import messages
from .models import DisciplinaryIncident, Sanction
from .forms import IncidentReportForm, SanctionForm


def report_incident(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Incident reported successfully!")
            return redirect('incident_list')
    else:
        form = IncidentReportForm()
    return render(request, 'core/report_incident.html', {'form': form})


def issue_sanction(request):
    if request.method == 'POST':
        form = SanctionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sanction issued successfully!")
            return redirect('incident_list')
    else:
        form = SanctionForm()
    return render(request, 'core/issue_sanction.html', {'form': form})
