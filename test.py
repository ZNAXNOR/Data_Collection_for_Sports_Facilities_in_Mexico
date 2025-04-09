import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class ChromeDriverManager:
    def __init__(self, chrome_path, chromedriver_path,
                 user_data_path=None, profile_directory=None, headless=False):
        self.chrome_path = chrome_path
        self.chromedriver_path = chromedriver_path
        self.user_data_path = user_data_path
        self.profile_directory = profile_directory
        self.headless = headless
        self.driver = None

    def create_driver(self):
        options = Options()
        options.binary_location = self.chrome_path

        if self.user_data_path and self.profile_directory:
            options.add_argument(f"--user-data-dir={self.user_data_path}")
            options.add_argument(f"--profile-directory={self.profile_directory}")

        if self.headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--remote-debugging-port=9222")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        service = Service(executable_path=self.chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()


class OpenYouTube:
    def __init__(self, driver):
        self.driver = driver

    def run(self):
        print("Opening YouTube...")
        self.driver.get("https://www.youtube.com")
        time.sleep(5)
        print("Done.")


def main():
    # === Configuration ===
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chromedriver_path = r"G:\OMKAR\Softwares\ChromeDriver\chromedriver-win64\chromedriver.exe"
    user_data_path = r"C:\Users\omkar.DESKTOP-RM76TAC\AppData\Local\Google\Chrome\User Data"
    profile_directory = "Profile 3"
    headless = False

    driver_manager = ChromeDriverManager(
        chrome_path=chrome_path,
        chromedriver_path=chromedriver_path,
        user_data_path=user_data_path,
        profile_directory=profile_directory,
        headless=headless
    )

    driver = None
    try:
        driver = driver_manager.create_driver()
        scraper = OpenYouTube(driver)
        scraper.run()

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        driver_manager.close_driver()


if __name__ == "__main__":
    main()
