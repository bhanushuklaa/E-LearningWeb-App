from dataclasses import field, fields
from pyexpat import model
from statistics import mode
#from tkinter import Widget
from django import forms
from .models import *
class DashboradForm(forms.Form):
    text = forms.CharField(label="Enter Your Search:")
    
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('female', 'Female'),
    ('Other', 'Other')
]
JOB_CITY_CHOICE= [
    ('Noida', 'Noida'),
    ('Channai', 'Channai'),
    ('Ranchi','Ranchi'),
    ('Pune', 'Pune'),
    ('Mumbai', 'Mumbai'),
    ('Banglore', 'Banglore'),
]
PROJECT_LANGUAGE_CHOICES= [
    ('C Language','C Language'),
    ('C++', 'C++'),
    ('C#','C#'),
    ('JAVA programming','JAVA programming'),
    ('PYTHON programming','PYTHON programming'),
    ('.NET Framework','.NET Framework'),
    ('PHP Programming','PHP Programming'),
    ('Machine Learning','Machine Learning'),
    ('Big DATA','Big DATA'),
    ('Django Framework','Django Framework'),
    ('Android','Android'),
    ('Digital Marketing','Digital Marketing'),
    ('Cloud Computing','Cloud Computing'),
    ('IOT','IOT'),
    ('WEB DEVELOPMENT','WEB DEVELOPMENT'),
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Location', choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    projects = forms.MultipleChoiceField(choices=PROJECT_LANGUAGE_CHOICES,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality',
        'city', 'pin', 'state', 'mobile','email', 'intro', 'qulification', 'clg_name', 'percentage',
        'job_city', 'profile_image','skills','projects', 'my_file']
        labels = {'name': 'Full name', 'dob': 'Date of Birth',
        'pin': 'Pin Code', 'mobile': 'Mobile No', 'email' : 'Email ID', 'intro': 'About Yourself', 'skills' : 'Your Skills',
        'qulification': 'Qulification', 'clg_name': 'School/Collage', 'percentage': 'CGPA/Percent','projects' : 'Projects','profile_image': 'Profile Image', 'my_file': 'Document'}
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'class':'form-control','id': 'datepicker'}),
            'locality' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'pin' : forms.NumberInput(attrs={'class':'form-control'}),
            'state' : forms.Select(attrs={'class':'form-control'}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'intro' : forms.Textarea(attrs={'class': 'form-control','placeholder': 'Introduce yourself and also tell about your  family background'}),
            'qulification' : forms.TextInput(attrs={'class':'form-control'}),
            'clg_name' : forms.TextInput(attrs={'class':'form-control'}),
            'percentage' : forms.TextInput(attrs={'class':'form-control'}),
            'skills' : forms.TextInput(attrs={'class':'form-control'}),
        }