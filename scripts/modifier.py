# Author: Andres Nicolas Alegre
# Date: 2023-08-10

from bs4 import BeautifulSoup

def modify_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    if soup.title:
        soup.title.string = "Modified Title"

    return soup.prettify()
