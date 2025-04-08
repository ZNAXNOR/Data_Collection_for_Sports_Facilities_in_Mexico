import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Precise paths
profile_path = r"C:\Users\omkar.DESKTOP-RM76TAC\AppData\Local\Google\Chrome\User Data"
profile_directory = "Profile 3"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chromedriver_path = r"G:\OMKAR\Softwares\ChromeDriver\chromedriver-win64\chromedriver.exe"

def get_driver(headless=True):
    """Initializes the Chrome WebDriver with specified user profile and optional headless mode."""
    options = Options()
    options.binary_location = chrome_path

    # Use existing Chrome profile
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument(f"--profile-directory={profile_directory}")

    # Chrome flags for stability and stealth
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Headless toggle
    if headless:
        options.add_argument("--headless=new")  # New headless mode (Chrome 109+)
        options.add_argument("--disable-gpu")

    # Debug logs
    print(f"Launching Chrome with profile: {profile_directory}")
    print(f"Chrome path: {chrome_path}")
    print(f"ChromeDriver path: {chromedriver_path}")

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def main():
    driver = None
    try:
        driver = get_driver(headless=False)  # Change to True for headless mode
        driver.get("https://www.youtube.com")
        time.sleep(5)  # Let the page load
    except Exception as e:
        print(f"Main Execution Error: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
