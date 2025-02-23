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
