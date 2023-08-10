# WebScraperToolkit

WebScraperToolkit is a comprehensive Python suite designed to dynamically extract HTML, CSS, and JavaScript content from websites. It not only fetches web content but also allows modifications to the extracted HTML. The scraped data, which includes the website's HTML structure, associated stylesheets (CSS), and JavaScript files or scripts, are saved in separate files. These files are organized within a directory, the name of which is specified by the user, and created on the user's desktop.

## Prerequisites

To run these scripts, you should have Python 3.6 or higher installed on your system.

Additionally, the following Python libraries and tools are required:

- BeautifulSoup
- requests
- selenium

To install these dependencies, execute the following command:

```bash
pip install beautifulsoup4 requests selenium
```

You will also need to have ChromeDriver installed and available in your system's PATH.

## How to Use

1. Clone this repository.
2. Navigate to the location of the `main.py` file in your terminal or command prompt.
3. Run the script using the command `python3 main.py`.
4. The script will prompt you to enter the name of the directory where the files should be stored. This directory will be created on your desktop.
5. Next, provide the URL of the website you want to scrape.
6. Post these inputs, the toolkit will dive into action, fetching the HTML, CSS, and JavaScript content from the site of your choice. The fetched data will be systematically saved in distinct files within the directory you named.

## File Descriptions

- **main.py**: The main script responsible for orchestrating the scraping process.
- **dynamic_extractor.py**: A script dedicated to scraping dynamically rendered content.
- **saver.py**: Saves the scraped data into respective files.
- **collector.py**: Collects content like HTML, CSS, and JS links.
- **modifier.py**: Provides functionality to make modifications to the scraped HTML content, such as changing the title.

## Contributions

Feel free to contribute if you'd like to help make the code better! Cheers!

## Licence

MIT

## Author

Andres Nicolas Alegre
@andresnalegre

