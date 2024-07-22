from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio', 'location', 'birth_date', 'profile_picture',
            'is_pro_diver', 'qualifications', 'dive_company', 'dive_shop_location',
            'certifications'
        ]
