from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Prompt user for topic to search
topic_search = input("Enter the topic to search: ")

# Replace spaces with '+' for the search query
topic_search = topic_search.replace(' ', '+')

# Set up Chrome options (optional, can be configured as needed)
chrome_options = Options()

# Provide the path to the ChromeDriver executable
service = Service('C:/Users/Praveena/Desktop/Publisher portal scrapper/chromedriver.exe')

# Initialize the Chrome WebDriver with the specified service and options
browser = webdriver.Chrome(service=service, options=chrome_options)

# Loop for pagination, use 0 to start from the first page
for i in range(1):  # Adjust the range as needed for multiple pages
    # Correct URL formation for pagination (i * 10 for each page)
    url = f"https://www.shiksha.com/search?q={topic_search}&start={i * 10}"
    # Open the search URL in the browser
    browser.get(url)

    # Wait for a few seconds to load the page
    time.sleep(3)

    # Extract the <div> elements that contain the links
    div_elements = browser.find_elements(By.CSS_SELECTOR, 'div.c8ff')  # Adjust this selector if necessary

    # Iterate through the div elements and extract widget label and URLs
    for div in div_elements:
        # Select the <a> tag inside the <div>
        link = div.find_element(By.TAG_NAME, 'a')
        # Extract the widget label and URL
        widget_label = link.get_attribute('widgetspecificlabel')
        href_url = link.get_attribute('href')
        print(f"College: {widget_label}, URL: {href_url}")

# Wait for a while to keep the browser open
time.sleep(10)  # Adjust this as needed to see the results

# Close the browser when done
browser.quit()
