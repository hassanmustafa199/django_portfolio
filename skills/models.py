from django.db import models

class Skill(models.Model):
    SKILL_TYPES = [
        ('technical', 'Technical'),
        ('professional', 'Professional'),
    ]

    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES)
    percentage = models.IntegerField(default=80)

    def __str__(self):
        return self.name