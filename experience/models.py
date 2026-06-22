from django.db import models

class Experience(models.Model):
    EXPERIENCE_TYPES = [
        ('academic', 'Academic'),
        ('professional', 'Professional'),
    ]

    title = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_TYPES)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title