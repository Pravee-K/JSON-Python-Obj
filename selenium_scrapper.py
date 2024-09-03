import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to perform search for a single college name
def search_college(driver, college):
    # Open Shiksha website
    driver.get('https://www.shiksha.com/')
    
    # Wait for the page to load completely
    time.sleep(5)  # Add an explicit wait for the entire page to load

    # Wait for the search input box to be present using a more specific selector if available
    try:
        # Update the selector with a more specific one based on inspection
        search_box = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#searchInput'))  # Example of a specific selector
        )
    except Exception as e:
        print(f"Error loading search box for {college}: {e}")
        # Debug: Print the current page source to understand the issue
        print(driver.page_source)
        return {'College': college, 'URL': 'Error - Search box not found'}

    # Clear the search box and enter the college name
    search_box.clear()
    search_box.send_keys(college)
    search_box.send_keys(Keys.ENTER)
    
    # Wait for the results page to load
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.tuple-title a'))  # Adjust this selector if needed
        )
    except Exception as e:
        print(f"Error loading results page for {college}: {e}")
        # Debug: Print the current page source to understand the issue
        print(driver.page_source)
        return {'College': college, 'URL': 'Error - Results page not loaded'}

    # Get the current URL of the results page
    results_page_url = driver.current_url
    
    # Print the result for debugging
    print(f"Processed: {college} - {results_page_url}")
    
    # Return the result
    return {'College': college, 'URL': results_page_url}

# Set up WebDriver (Ensure ChromeDriver is installed and in your PATH)
driver = webdriver.Chrome()  # Or use any other driver like Firefox

# Test with a Single College Name
single_college_name = "Coimbatore Institute of Technology"  # Replace with a single college name for testing
single_result = search_college(driver, single_college_name)
print(f"Single test result: {single_result}")

# Close the browser
driver.quit()
