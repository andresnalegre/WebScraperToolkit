# Author: Andres Nicolas Alegre
# Date: 2023-08-10

import os

def save_data(directory, html_content, stylesheets, javascripts):
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, 'code.html'), 'w') as file:
        file.write(html_content)

    all_styles = "\n".join(stylesheets)
    with open(os.path.join(directory, 'code.css'), 'w') as file:
        file.write(all_styles)

    all_scripts = "\n".join(javascripts)
    with open(os.path.join(directory, 'code.js'), 'w') as file:
        file.write(all_scripts)
