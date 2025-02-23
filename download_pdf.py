# Importing Libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
import base64  # Required for decoding the base64 PDF data

# Configuration
brave_path = "Your Browser Path Here (I use brave thus i have brave Path)"
chromedriver_path = "Your Chrome Drivers Path Here"
output_folder = "Download Directory"
os.makedirs(output_folder, exist_ok=True)  # Ensure folder exists

# Set up Selenium options for Brave
brave_options = webdriver.ChromeOptions()
brave_options.binary_location = brave_path
brave_options.add_argument("--headless")  
brave_options.add_argument("--disable-gpu")  

# Initialize WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=brave_options)

# User input
n = int(input("How many pages to print: "))

# Rate limiting variables
refresh_count = 0
start_time = time.time()

for i in range(1, n + 1):
    # This is my project https://github.com/anasskhannn/Daily-Reflection-Journal
    driver.get("https://daily-reflection-journal.netlify.app/book")
    time.sleep(2)  

    # Print page to PDF
    pdf_path = os.path.join(output_folder, f"{i}.pdf")
    print_params = {
        "landscape": False,
        "displayHeaderFooter": False,
        "printBackground": True,
        "preferCSSPageSize": True,
    }
    
    pdf_data = driver.execute_cdp_cmd("Page.printToPDF", print_params)["data"]
    pdf_bytes = base64.b64decode(pdf_data)  

    with open(pdf_path, "wb") as f:
        f.write(pdf_bytes)

    print(f"Saved: {pdf_path}")

    # Refresh the page (if not last iteration)
    if i < n:
        driver.refresh()
        refresh_count += 1  
