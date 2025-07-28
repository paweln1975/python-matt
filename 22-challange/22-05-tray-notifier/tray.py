# tray.py
import requests
import asyncio
from plyer import notification
from desktop_notifier import DesktopNotifier

URL = 'http://dl1b5yy03.aptiv.com:8000/hw_store'  # Replace with your target URL
notifier = DesktopNotifier()

async def show_tray_notification(title, message):
    await notifier.send(title=title, message=message)
    # notification.notify(
    #     title='Website Down',
    #     message=f'{URL} is not accessible!',
    #     app_name='Site Monitor',
    #     timeout=5
    # )

def check_website(url):
    try:
        # print status message
        print(f'Checking {url} ...')
        response = requests.get(url, timeout=5)
        # print response status code
        print(f'Status code: {response.status_code}')
        return response.status_code == 200
    except requests.RequestException:
        return False

async def monitor():
    while True:
        if not check_website(URL):
            await show_tray_notification(
                title='Website Down',
                message=f'{URL} is not accessible!'
            )
        await asyncio.sleep(10)  # 30 seconds interval

if __name__ == '__main__':
    asyncio.run(monitor())
