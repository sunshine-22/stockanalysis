from django.db import models

# Create your models here.
class graphdata(models.Model):
    csvfile=models.FileField(upload_to="visualizations/")
