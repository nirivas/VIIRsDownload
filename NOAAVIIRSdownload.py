import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description='Download files from a website.')
parser.add_argument('url', type=str, help='The URL of the website to scrape')
parser.add_argument('download_dir', type=str, help='The directory where downloaded files will be saved')
args = parser.parse_args()

# Get the URL and download directory from command-line arguments
website_url = args.url
download_dir = args.download_dir

# Ensure the download directory exists
os.makedirs(download_dir, exist_ok=True)

# Set up Chrome options
chrome_options = Options()

# Set Chrome preferences to change download directory
chrome_prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", chrome_prefs)

# Automatically manage ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the website
driver.get(website_url)

# Wait for the dropdown to be present
dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'indexlist_length'))  # Locating by the name attribute
)

# Create a Select object and choose the 'All' option
select = Select(dropdown)
select.select_by_value('-1')  # '-1' corresponds to the 'All' option in the provided HTML

# Store all links that start with '2013'
def fetch_links():
    return [link.get_attribute("href") for link in driver.find_elements(By.TAG_NAME, "a") if link.get_attribute("href") and link.get_attribute("href").endswith('.nc')]

# Wait for the page to update after selecting 'All'
time.sleep(2)  # Adjust this sleep if needed, or use explicit waits if the page has dynamic content

links = fetch_links()

# Loop through the links and navigate
for href in links:
    try:
        print(f"Clicking on: {href}")
        driver.get(href)
        
        # Wait for some condition if needed, e.g., an element on the new page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        
        driver.back()  # Go back to the original page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))  # Wait for links to reload
        
        # Refetch the links after going back to avoid stale elements
        links = fetch_links()
        
    except Exception as e:
        print(f"Failed to click on: {href}, error: {e}")

driver.quit()
