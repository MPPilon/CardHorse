from django.db import models


class DBErrorLog(models.Model):
    WARNING = 'Warning'
    LOW = 'Low'
    MODERATE = 'Moderate'
    SEVERE = 'Severe'

    severity = models.CharField(max_length=20, default='Severe')  # Defaults severe so I don't fuck up
    error = models.CharField(max_length=200)