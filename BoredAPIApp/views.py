
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import User, Activity
from .utils import fetch_activities
from .forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity
from .forms import ActivityForm
from django.utils import timezone


def register_user(request):
    activity_types = [
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
    if request.method == 'POST':
        # Process the registration form data
        # username = request.POST['username']
        form = RegistrationForm(request.POST)
        if form.is_valid():
            activities = form.cleaned_data['activities']
            email = request.POST['email']
            registration_type = request.POST['activity_type']

        # Create a new User instance
            user = User.objects.create(email=email, registration_type=registration_type)

        # Fetch 10 activities based on the selected type and associate them with the User
            activities = fetch_activities(registration_type, 10)
            for activity in activities:
                Activity.objects.create(user=user, name=activity['name'], description=activity['description'])

        # Send a welcome email to the User
            send_mail(
                'Welcome to BoredAPI App',
                'Thank you for registering!',
                'admin@boredapi.com',
                [email],
                fail_silently=False,
            )

        return redirect('activities_listing')
    return render(request, 'register.html', {'activity_types': activity_types, 'error': 'Please fill in all fields'})

@login_required
def activities_listing(request):
    try:
        user = User.objects.get(email=request.user.email)
        activities = Activity.objects.filter(user=user)
        return render(request, 'activities.html', {'activities': activities})
    except User.DoesNotExist:
        return render(request, 'activities.html', {'error': 'User does not exist'})



@login_required
def fetch_more_activities(request):
    try:
        user = User.objects.get(email=request.user.email)
        today = timezone.now().date()
        activities_today = Activity.objects.filter(user=user, created_at__date=today).count()
        if activities_today < 2:
            registration_type = user.registration_type
            new_activities = fetch_activities(registration_type, 2)
            for activity in new_activities:
                Activity.objects.create(user=user, name=activity['name'], description=activity['description'])
            return redirect('activities_listing')
        else:
            warning_message = "You have reached the limit of fetching activities for today."
            return render(request, 'warning.html', {'warning_message': warning_message})
    except User.DoesNotExist:
        return HttpResponse('User does not exist')







def edit_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activities_listing')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'edit_activity.html', {'form': form})




def view_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    return render(request, 'view_activity.html', {'activity': activity})

def delete_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    activity.delete()
    return redirect('activities_listing')
