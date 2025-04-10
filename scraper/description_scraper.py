import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from tqdm import tqdm

# Set up Selenium WebDriver (Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in background
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
service = Service()
driver = webdriver.Chrome(service=service, options=options)

# Load the catalogue file
df = pd.read_csv("data/updated_assessment_catalog.csv")

def scrape_description(url):
    try:
        driver.get(url)
        time.sleep(2)

        # 🛑 Handle cookie popup if it appears
        try:
            cookie_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
            cookie_button.click()
            print("✅ Cookie popup accepted.")
            time.sleep(1)
        except NoSuchElementException:
            print("ℹ️ No cookie popup found.")

        # ✅ Try scraping the product description
        try:
            description_div = driver.find_element(By.CLASS_NAME, "product-description")
            description = description_div.text.strip()
        except Exception:
            description = "No Description Found"

        return description

    except Exception as e:
        print(f"❌ Error scraping {url}: {str(e)}")
        return "No Description Found"

# Apply scraping to each row in the DataFrame
descriptions = []
for url in tqdm(df["url"], desc="Scraping descriptions"):
    descriptions.append(scrape_description(url))

# Add descriptions back to DataFrame
df["description"] = descriptions

# Save updated data to new CSV
df.to_csv("final_assessment_catalogue_with_descriptions.csv", index=False)
print("✅ Done! Descriptions saved to 'final_assessment_catalogue_with_descriptions.csv'")

# Close browser
driver.quit()
