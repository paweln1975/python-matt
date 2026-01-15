import requests
import re
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class WebScraperTemplate(ABC):
    def scrape(self, url):
        content = self.load_page(url)
        data = self.parse_content(content)
        self.extract_data(data)

    @abstractmethod
    def load_page(self, url):
        pass

    @abstractmethod
    def parse_content(self, content):
        pass

    @abstractmethod
    def extract_data(self, data):
        pass


class BeautifulSoupScraper(WebScraperTemplate):
    def load_page(self, url):
        print(f"Loading page from {url} using requests.")
        response = requests.get(url)
        return response.content

    def parse_content(self, content):
        print("Parsing content using BeautifulSoup.")
        return BeautifulSoup(content, "html.parser")

    def extract_data(self, data):
        print("Extracting data from parsed HTML using BeautifulSoup.")
        title = data.title
        print(f"Page Title: {title.string}")
        for link in data.find_all('a'):
            print(f"Link: {link.get('href')}")

class RegexpScraper(WebScraperTemplate):
    def load_page(self, url):
        print(f"Loading page from {url} using requests.")
        response = requests.get(url)
        return response.text

    def parse_content(self, content):
        print("No Parsing content.")
        return content

    def extract_data(self, data):
        print("Extracting data from parsed HTML using regular expressions.")

        title_match = re.search(r'<title>(.*?)</title>', data)
        if title_match:
            print(f"Page Title: {title_match.group(1)}")
        links = re.findall(r'href=["\'](.*?)["\']', data)
        for link in links:
            print(f"Link: {link}")

if __name__ == "__main__":
    url = "http://10.224.185.56/"
    scraper = BeautifulSoupScraper()
    scraper.scrape(url)

    print("\n" + "="*50 + "\n")
    scraper = RegexpScraper()
    scraper.scrape(url)

