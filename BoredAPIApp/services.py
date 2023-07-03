# services.py

import requests

def fetch_activities(activity_type, limit):
    url = f'https://www.boredapi.com/api/activity?type={activity_type}&participants=1&price=0.0&limit={limit}'

    try:
        response = requests.get(url)
        data = response.json()

        if 'results' in data:
            return data['results']
        else:
            return []

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []
