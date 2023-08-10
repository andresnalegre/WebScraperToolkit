# Author: Andres Nicolas Alegre
# Date: 2023-08-10

from selenium import webdriver
import os

def extract_dynamic_content(url, directory_name):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    html_content = driver.page_source
    driver.quit()

    desktop_path = os.path.join("/Users/andresnicolasalegre/Desktop", directory_name)
    os.makedirs(desktop_path, exist_ok=True)

    with open(os.path.join(desktop_path, "code.html"), "w") as file:
        file.write(html_content)

    print("Dynamic HTML file successfully saved on Desktop!")

