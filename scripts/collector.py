# Author: Andres Nicolas Alegre
# Date: 2023-08-10

import requests
from bs4 import BeautifulSoup

def collect_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    html_content = soup.prettify()
    stylesheets = [link["href"] for link in soup.find_all("link", rel="stylesheet") if "href" in link.attrs]
    javascripts = [script["src"] for script in soup.find_all("script") if "src" in script.attrs]
    
    return html_content, stylesheets, javascripts
