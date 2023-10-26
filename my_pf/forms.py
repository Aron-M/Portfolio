from django import forms
from .models import PersonalDetails, Headings, Skills, Project


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = '__all__'

class HeadingsForm(forms.ModelForm):
    class Meta:
        model = Headings
        exclude = []  # Exclude all fields by default
        widgets = {
            'big_header': forms.Textarea(attrs={'rows':3, 'cols': 60}),
            'sub_header': forms.Textarea(attrs={'rows':3, 'cols': 60}),
            'par1': forms.Textarea(attrs={'rows': 3, 'cols': 60}),
            'par2': forms.Textarea(attrs={'rows': 3, 'cols': 60}),
            'par3': forms.Textarea(attrs={'rows': 3, 'cols': 60}),
            'par4': forms.Textarea(attrs={'rows': 3, 'cols': 60}),
            'par5': forms.Textarea(attrs={'rows': 3, 'cols': 60}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_image'].required = False

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'


class SkillIconForm(forms.Form):
    skills_icon = forms.URLField(max_length=100, required=False)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'description', 'extra_info', 'live_site', 'github_url']
