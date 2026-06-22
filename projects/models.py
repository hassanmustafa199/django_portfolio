from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    description = models.TextField()
    technology_used = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title