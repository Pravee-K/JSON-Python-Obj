import pandas as pd
import asyncio
from playwright.async_api import async_playwright

# Function to perform search and get URLs
async def get_college_urls(college_names):
    urls = []
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Change to True for headless mode
        page = await browser.new_page()

        for college in college_names:
            try:
                # Navigate to Shiksha's homepage
                await page.goto('https://www.shiksha.com/')
                
                # Find the search bar and enter the college name
                await page.fill('input[type="search"]', college)
                await page.keyboard.press('Enter')
                await page.wait_for_load_state('networkidle')  # Wait for results to load

                # Extract all search results
                search_results = await page.query_selector_all('.tuple-title a')

                # Initialize a variable to store the URL of the exact match
                college_url = 'URL not found'
                
                # Loop through search results to find the exact match
                for result in search_results:
                    result_name = await result.inner_text()
                    if college.lower() in result_name.lower():  # Adjust matching logic as needed
                        await result.click()  # Click on the matching result to navigate to the page
                        await page.wait_for_load_state('networkidle')  # Wait for the page to load
                        college_url = page.url  # Get the current URL of the college page
                        await page.go_back()  # Go back to the search results page
                        await page.wait_for_load_state('networkidle')  # Wait for the results page to load again
                        break  # Exit the loop after finding the first match

                # Store the result
                urls.append({'College': college, 'URL': college_url})
                print(f"Retrieved URL for {college}: {college_url}")

            except Exception as e:
                print(f"Error processing {college}: {e}")
                urls.append({'College': college, 'URL': 'Error'})

        await browser.close()
    
    return urls

# Main function to read CSV and call the search function
async def main():
    # Load the CSV file containing college names
    df = pd.read_csv('colleges.csv')  # Replace 'colleges.csv' with your file path
    college_names = df['CollegeName'].tolist()  # Replace 'CollegeName' with the column name in your CSV

    # Retrieve URLs
    results = await get_college_urls(college_names)

    # Convert results to a DataFrame and save to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv('college_urls_playwright.csv', index=False)
    print("Saved results to college_urls_playwright.csv")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
