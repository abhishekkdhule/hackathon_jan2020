from django import forms
from .models import *

class Faculty_login_form(forms.ModelForm):
    fac_password=forms.CharField(max_length=10, widget=forms.PasswordInput)
    class Meta:
        
        model=Faculty_profile_model
        fields=[
            'fac_id',
            'fac_password',
        ]
class Faculty_profile_form(forms.ModelForm):
    class Meta:
        model=Faculty_profile_model
        fields=[
            'total_lecures'
        ]
        
# class Faculty_dox_form(forms.ModelForm):
#     class Meta:
#         model=Faculty_profile_model
#         fields=[
#             'fac_file_name1',
#             'fac_file1',
#             'fac_file_name2',
#             'fac_file2',
#         ]