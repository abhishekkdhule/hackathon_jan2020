from django import forms
from .models import *

class Student_login_form(forms.ModelForm):
    std_password=forms.CharField(max_length=10, widget=forms.PasswordInput)
    class Meta:
        model = Students_profile_model
        fields = [
            'std_id',
            'std_password'
        ]



CHOICES=[(1,'present'),
         (0,'absent')]
class Std_attendance_form(forms.Form):
    # is_present = forms.ChoiceField(choices=CHOICES,required=False, widget=forms.CheckboxInput())
    is_present=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())


class Student_academics_form(forms.ModelForm):
    class Meta:
        model=Students_profile_model
        fields=[
            's1_tt1',
            's1_tt2',
            's1_sem1',
            
            's2_tt1',
            's2_tt2',
            's2_sem1',
            
            's3_tt1',
            's3_tt2',
            's3_sem1',
            
            's4_tt1',
            's4_tt2',
            's4_sem1',
            
            's5_tt1',
            's5_tt2',
            's5_sem1',
            
            's6_tt1',
            's6_tt2',
            's6_sem1',
            
        ]
        