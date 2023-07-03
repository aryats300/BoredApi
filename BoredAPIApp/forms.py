from django import forms
from .models import Activity

class RegistrationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    activity_type = forms.ChoiceField(
        label='Activity Type',
        choices=[
            ('education', 'Education'),
            ('recreational', 'Recreational'),
            ('social', 'Social'),
            ('diy', 'DIY'),
            ('charity', 'Charity'),
            ('cooking', 'Cooking'),
            ('relaxation', 'Relaxation'),
            ('music', 'Music'),
            ('busywork', 'Busywork'),
        ]
    )


# boredapi_app/forms.py



class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'description']  # Update the fields as per your Activity model
