from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='projects')
    demo_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Create your models here.
