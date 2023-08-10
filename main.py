# Author: Andres Nicolas Alegre
# Date: 2023-08-10

import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def download_file(url, path):
    local_filename = os.path.join(path, url.split('/')[-1])
    with requests.get(url, stream=True, verify=False) as r:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def download_css_js(path, soup, website):
    for link in soup.find_all('link', href=True):
        if link['href'].startswith("http"):
            css_url = link['href']
        else:
            css_url = website + link['href']
        local_file = download_file(css_url, path)
        link['href'] = os.path.basename(local_file)

    for script in soup.find_all('script', src=True):
        if script['src'].startswith("http"):
            js_url = script['src']
        else:
            js_url = website + script['src']
        local_file = download_file(js_url, path)
        script['src'] = os.path.basename(local_file)

def main():
    directory_name = input("Enter the name of the directory you wish to create: ")
    website = input("Enter the URL of the website you wish to extract: ")

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    path = os.path.join(desktop_path, directory_name)

    if not os.path.exists(path):
        os.makedirs(path)

    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    browser = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'), options=options)
    browser.get(website)
    source = browser.page_source
    browser.quit()

    soup = BeautifulSoup(source, 'html.parser')
    
    download_css_js(path, soup, website)
    
    with open(os.path.join(path, 'code.html'), 'w', encoding='utf-8') as f:
        f.write(str(soup))

    with open(os.path.join(path, 'code.js'), 'w', encoding='utf-8') as fjs:
        for script in soup.find_all('script'):
            if not script.get('src'):
                fjs.write(script.string)

    with open(os.path.join(path, 'code.css'), 'w', encoding='utf-8') as fcss:
        for style in soup.find_all('style'):
            fcss.write(style.string)

if __name__ == '__main__':
    main()
