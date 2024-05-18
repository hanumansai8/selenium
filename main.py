import time
import logging
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("selenium_test.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger()

# Path to your ChromeDriver executable
driver_path = 'D:\\chrome-win64\\chromedriver.exe'
#options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

try:
    # Start time to measure response time
    start_time = time.time()

    # Open website
    driver.get("https://atg.party")

    # Log HTTP response code and response time
    response = requests.get("https://atg.party")
    response_time = time.time() - start_time
    logger.info(f"HTTP Response Code: {response.status_code}")
    logger.info(f"Response Time: {response_time:.2f} seconds")

    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'outer-header__loginbtn'))
    )
    login_button.click()

    # Wait for the email input box to appear and enter the email
    email_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email_landing"))
    )
    email_box.send_keys("wiz_saurabh@rediffmail.com")

    # Find the password input box and enter the password
    pass_box = driver.find_element(By.ID, "password_landing")
    pass_box.send_keys("Pass@123")

    # Find the login button in the modal and click it
    login_button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'landing-signin-btn'))
    )
    login_button1.click()
    time.sleep(10)

    # Wait for the next page to load (adjust the locator as needed)
    driver.get("http://atg.party/article")
    time.sleep(10)

    # Post an article
    title_input = input("Enter your title:")
    title_key = driver.find_element(By.ID, "title")
    title_key.send_keys(title_input)
    time.sleep(10)

    share_on = driver.find_element(By.CLASS_NAME, "cdx-block")
    share_input = input("Share your thought:")
    share_on.send_keys(share_input)
    time.sleep(3)
    logger.info("Article posted successfully")


    cover_image_path = input("Enter your destination of cover photo:")

    cover_image = driver.find_element(By.CLASS_NAME, "add-cover-image")
    cover_image.send_keys(cover_image_path)
    logger.info("Article posted successfully")


    post_button = driver.find_element(By.ID, "hpost_btn")
    post_button.click()

    logger.info("Article posted successfully")

finally:
    # Quit the browser
    driver.quit()
