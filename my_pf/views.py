from django.shortcuts import render, get_object_or_404, redirect
from .models import PersonalDetails, Headings, Project, Skills, SkillCategory
from .forms import PersonalDetailsForm, HeadingsForm, SkillsForm, ProjectForm
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect

def redirect_if_not_admin(fn):
    def wrapper(request):
        if request.user.is_superuser:
            return fn(request)
        else:
            return HttpResponseRedirect('/')
    return wrapper


def display_me_irl(request):
    data = PersonalDetails.objects.all()
    context = {'data': data}
    return render(request, 'pages/me-irl.html', context)

def display_skills_page(request):
    return render(request, 'pages/skills.html')

def display_all(request):
    data = PersonalDetails.objects.all()
    skills = Skills.objects.all()
    category = SkillCategory.objects.all()
    projects = Project.objects.all()
    headings = Headings.objects.all()
    context = {
        'data': data, 'headings': headings, 'projects': projects, 'skills': skills, 'category': category
        }
    if request.path == "home/":
        return render(request, 'pages/home-page.html', context )
    else: 
        return render(request, 'pages/home-page.html', context )


@redirect_if_not_admin
def dashboard_view(request):
    skills = Skills.objects.all()
    project = Project.objects.all()
    context = {
        'project': project, 'skills': skills
    }

    return render(request, 'pages/dashboard.html')


def display_edit_personal_details(request):
    detail = get_object_or_404(PersonalDetails)
    data = PersonalDetails.objects.all()

    if request.method == 'POST':
        personal_details_form = PersonalDetailsForm(request.POST, request.FILES, instance=detail)
        if personal_details_form.is_valid():
            if 'image' in request.FILES:
                detail.image = request.FILES['image']
            personal_details_form.save()
            return redirect('edit-personal-details')
    else:
        personal_details_form = PersonalDetailsForm(instance=detail)

    context = {
        'data': data,
        'personal_details_form': personal_details_form
    }

    return render(request, 'pages/edit-personal-details.html', context)



def display_edit_headings(request):
    all_headings = Headings.objects.all()
    heading = get_object_or_404(Headings)

    if request.method == 'POST':
        headings_form = HeadingsForm(request.POST, request.FILES, instance=heading)
        if headings_form.is_valid():
            print("Valid Form")
            headings_form.save()
            return redirect('edit-headings')
    else:
        headings_form = HeadingsForm(instance=heading)

    context = {
        'headings': all_headings,
        'headings_form': headings_form
    }

    return render(request, 'pages/edit-headings.html', context)


def add_skill(request):
    skills = Skills.objects.all()
    skills_form = SkillsForm()
    category = SkillCategory.objects.all()
    if request.method == 'POST':
        skills_form = SkillsForm(request.POST)
        if skills_form.is_valid():
            skills_form.save()
            return redirect('add-skill')
    else:
        context = {
            'skills': skills,
            'skills_form': skills_form,
            'category': category
        }
        return render(request, 'pages/add-skill.html', context)


def add_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.image = request.FILES['image']
            project.save()
            return redirect('add-project')
    else:
        project_form = ProjectForm()

    projects = Project.objects.all()
    context = {
        'projects': projects,
        'project_form': project_form
    }
    return render(request, 'pages/add-project.html', context)


def display_edit_skills(request, skill_id=None):
    skills = Skills.objects.all()
    category = SkillCategory.objects.all()
    
    if skill_id:
        skill = get_object_or_404(Skills, id=skill_id)
        skills_form = SkillsForm(instance=skill)
    else:
        skills_form = SkillsForm()
    
    if request.method == 'POST':
        if skill_id:
            skill = get_object_or_404(Skills, id=skill_id)
            skills_form = SkillsForm(request.POST, request.FILES, instance=skill)
        else:
            skills_form = SkillsForm(request.POST, request.FILES)
        
        if skills_form.is_valid():
            skills_form.save()
            messages.success(request, 'Skills updated successfully.')
            if skill_id:
                return redirect('edit-skills', skill_id=skill.id)
            else:
                return redirect('edit-skills')
        else:
            messages.error(request, 'Error updating skills.')
    
    context = {
        'skill': skill if skill_id else None,
        'skills_form': skills_form,
        'category': category,
        'skills': skills
    }
    return render(request, 'pages/edit-skills.html', context)


def delete_skill(request, skill_id=None):
    skills = Skills.objects.all()
    category = SkillCategory.objects.all()

    if skill_id:
        skill = get_object_or_404(Skills, id=skill_id)
        skills_form = SkillsForm(instance=skill)
    else:
        skills_form = SkillsForm()

    if request.method == 'POST':
        if skill_id:
            skill.delete()
            return redirect('delete-skill')
    
    context = {
        'skill': skill if skill_id else None,
        'skills_form': skills_form,
        'category': category,
        'skills': skills
    }
    return render(request, 'pages/delete-skill.html', context)


def display_edit_projects(request, project_id=None):
    projects = Project.objects.all()

    if project_id:
        project = get_object_or_404(Project, id=project_id)
        project_form = ProjectForm(instance=project)
    else:
        project_form = ProjectForm()

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES, instance=project)
        if project_form.is_valid():
            project_form.save()
            return redirect('edit-projects', project_id=project.id)
        else:
            messages.error(request, 'Error updating projects.')

    context = {
        'projects': projects,
        'project_form': project_form,
        'project': project if project_id else None,
    }
    return render(request, 'pages/edit-projects.html', context)


def delete_project(request, project_id=None):
    projects = Project.objects.all()

    if project_id:
        project = get_object_or_404(Project, id=project_id)
        project_form = ProjectForm(instance=project)
    else:
        project_form = ProjectForm()

    if request.method == 'POST':
        if project_id:
            project.delete()
            return redirect('delete-project')
    
    context = {
        'project': project if project_id else None,
        'projects': projects,
        'project_form': project_form,
    }
    return render(request, 'pages/delete-project.html', context)





