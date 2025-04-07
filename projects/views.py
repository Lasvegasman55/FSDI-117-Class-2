from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Skill
from django.contrib import messages
from .forms import ProjectForm
from django.core.files import File
# This import is redundant since you already have ".models import Project" above
# from projects.models import Project  
from django.urls import reverse
from django.http import HttpResponseRedirect  # Fixed typo here

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_form.html', {'form': form})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def update_project_images(request):
    # Only allow admin users to run this
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('project_list'))  # Changed to project_list based on your view names
    
    try:
        # Get your projects by title
        task_project = Project.objects.get(title='Task Management App')
        ecommerce_project = Project.objects.get(title='E-commerce Website')
        weather_project = Project.objects.get(title='Weather Dashboard')
        
        # Update images - replace paths with your actual image locations
        with open('task-management-icon.png', 'rb') as img_file:
            task_project.image.save('task-management-icon.png', File(img_file), save=True)
            
        with open('ecommerce-icons.png', 'rb') as img_file:
            ecommerce_project.image.save('ecommerce-icons.png', File(img_file), save=True)
            
        with open('weather-icon.png', 'rb') as img_file:
            weather_project.image.save('weather-icon.png', File(img_file), save=True)
            
        # Add a success message
        messages.success(request, "Project images updated successfully")
    
    except Exception as e:
        # Handle errors
        messages.error(request, f"Error updating project images: {e}")
        print(f"Error updating project images: {e}")
    
    # Redirect back to projects page
    return HttpResponseRedirect(reverse('project_list'))  # Changed to project_list based on your view names