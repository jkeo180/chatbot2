import bs4 as BeautifulSoup
import selenium as selenium
import selenium.webdriver as webdriver
import requests

def fetch_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch page content: {response.status_code}")
def parse_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup
def extract_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        links.append(a_tag['href'])
    return links