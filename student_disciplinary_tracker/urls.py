from django.urls import path
from .views import report_incident, issue_sanction

urlpatterns = [
    path('report-incident/', report_incident, name='report_incident'),
    path('issue-sanction/', issue_sanction, name='issue_sanction'),
]
