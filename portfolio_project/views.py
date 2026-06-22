from django.shortcuts import render
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project

def home(request):
    context = {
        'bio': Bio.objects.first(),
        'education': Education.objects.all(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
    }
    return render(request, 'index.html', context)