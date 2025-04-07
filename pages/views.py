from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Skill
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

# For the extra challenge - function-based view to add a project
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

def home(request):
    """View function for the homepage"""
    return render(request, 'pages/about_me.html')



def contact(request):
    """View function for the contact page"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

    

            
            
            # Send email
            try:
                send_mail(
                    f'Contact Form: Message from {name}',
                    f'From: {name} <{email}>\n\n{content}',
                    email,  # From email
                    ['MichaelMatthews2024@gmail.com'],  # To email
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
    else:
        form = ContactForm()
    
    return render(request, 'pages/contact.html', {
        'form': form
    })