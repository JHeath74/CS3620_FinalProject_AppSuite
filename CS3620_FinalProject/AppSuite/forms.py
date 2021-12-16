from django import forms
from .models import Profile, Journal, Hiking


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone', 'summary', 'degree', 'school', 'university', 'previous_work', 'skills']


class HikeForm(forms.ModelForm):
    class Meta:
        model = Hiking
        fields = ['Hike_Name', 'Hike_Length', 'Hike_TrailType', 'Hike_TimeOfYear', 'Hike_Difficulty', 'Hike_TrailHead',
                  'Hike_Completed', 'Hike_Notes', 'Hike_Images']


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['Date_Time', 'Journal_Entry']

