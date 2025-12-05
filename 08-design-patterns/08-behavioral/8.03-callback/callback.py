from typing import Any, Callable
from urllib.request import urlopen

class CallbackDownloader:
    def __init__(self, url: str,
                 on_success: Callable[[str], Any] = lambda data: ...,
                 on_error: Callable[[Exception], Any] = lambda err: ...
                 ) -> None:
        self.url = url
        self.callback_on_success = on_success
        self.callback_on_error = on_error

    def download(self) -> None:
        try:
            with urlopen(self.url) as response:
                data = response.read().decode('utf-8')
        except Exception as error:
            self.callback_on_error(error)
        else:
            self.callback_on_success(data)


def ok(data: str) -> None:
    print(f'Downloaded {len(data)} characters')
    print('=' * 80)
    print(f'First 100 characters:\n{data[:100]}')
    print('=' * 80)

def error(err: Exception) -> None:
    print(f'Error occurred: {err}')

# Example usage:
downloader = CallbackDownloader(
    url='https://python3.info',
    on_success=ok,
    on_error=error
)

downloader.download()

downloader = CallbackDownloader(
    url='http://python3.info/non-existing-page',
    on_error=error)

downloader.download()

