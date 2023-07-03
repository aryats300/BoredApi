# boredapi_project/urls.py
from django.urls import path
from .views import (
    register_user,
    activities_listing,
    fetch_more_activities,
    edit_activity,
    view_activity,
    delete_activity
)

urlpatterns = [
    path('register/', register_user, name='register'),
    path('activities/', activities_listing, name='activities_listing'),
    path('fetch-more-activities/', fetch_more_activities, name='fetch_more_activities'),
    path('edit-activity/<int:activity_id>/', edit_activity, name='edit_activity'),
    path('view-activity/<int:activity_id>/', view_activity, name='view_activity'),
    path('delete-activity/<int:activity_id>/', delete_activity, name='delete_activity'),
]
# from django.urls import path
# from .views import register_user

# urlpatterns = [
#     path('register/', register_user, name='register'),