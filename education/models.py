from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=150)
    institute = models.CharField(max_length=150)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree