from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=20)
    section = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.grade_level} - {self.section})"


class SeverityLevel(models.Model):
    level_id = models.AutoField(primary_key=True)
    level_description = models.CharField(max_length=50)  

    def __str__(self):
        return self.level_description


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=[('POD', 'Prefect of Discipline'), ('Admin', 'Administrator')])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  

    def __str__(self):
        return f"{self.name} ({self.role})"


class DisciplinaryIncident(models.Model):
    incident_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="incidents")
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    severity_level = models.ForeignKey(SeverityLevel, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="reported_incidents")

    def __str__(self):
        return f"Incident {self.incident_id} - {self.student.name} ({self.severity_level.level_description})"


class Sanction(models.Model):
    sanction_id = models.AutoField(primary_key=True)
    incident = models.ForeignKey(DisciplinaryIncident, on_delete=models.CASCADE, related_name="sanctions")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="sanctions")
    description = models.TextField()
    duration = models.PositiveIntegerField()  # Duration in days ni
    severity_level = models.ForeignKey(SeverityLevel, on_delete=models.CASCADE)
    issued_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="issued_sanctions")

    def clean(self):
        """ Business rule enforcement for sanction duration """
        if self.severity_level.level_description == "Minor" and not (1 <= self.duration <= 2):
            raise ValidationError("Minor sanctions must have a duration of 1-2 days.")
        elif self.severity_level.level_description == "Moderate" and not (3 <= self.duration <= 5):
            raise ValidationError("Moderate sanctions must have a duration of 3-5 days.")
        elif self.severity_level.level_description == "Severe" and self.duration < 7:
            raise ValidationError("Severe sanctions must have a duration of 7 days or more.")

    def __str__(self):
        return f"Sanction {self.sanction_id} - {self.student.name} ({self.severity_level.level_description})"
