# tray.py
import time
import requests
from plyer import notification

URL = 'http://dl1b5yy03.aptiv.com:8000/hw_store'  # Replace with your target URL

def check_website(url):
    try:
        # print status message
        print(f'Checking {url} ...')
        response = requests.get(url, timeout=10)
        # print response status code
        print(f'Status code: {response.status_code}')
        return response.status_code == 200
    except requests.RequestException:
        return False

while True:
    if not check_website(URL):
        notification.notify(
            title='Website Down',
            message=f'{URL} is not accessible!',
            app_name='Site Monitor',
            timeout=5
        )
    time.sleep(5)
