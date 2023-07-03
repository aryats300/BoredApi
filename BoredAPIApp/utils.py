# boredapi_app/boredapi_utils.py
import requests

def fetch_activities(activity_type, limit):
    url = f'https://www.boredapi.com/api/activity?type={activity_type}&participants=1&price=0.0&accessibility=0.0&limit={limit}'
    response = requests.get(url)
    data = response.json()
    activities = data['activities']
    return activities
