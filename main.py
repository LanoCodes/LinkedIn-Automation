from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time, os, random

random_sleep = [2, 3, 4]

url_linkedin = "https://www.linkedin.com/jobs/search/?distance=25&f_AL=true&geoId=106224388&keywords=python%20developer&location=Atlanta%2C%20Georgia%2C%20United%20States&refresh=true&sortBy=R"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url_linkedin)
sign_in_button_0 = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button_0.click()
time.sleep(random.choice(random_sleep))

linked_in_user = os.environ.get('LINKEDIN_USER')
linked_in_login = os.environ.get('LINKEDIN_PASS')
email_box = driver.find_element(By.ID, "username")
password_box = driver.find_element(By.ID, "password")
email_box.send_keys(linked_in_user)
password_box.send_keys(linked_in_login)

sign_in_button_1 = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
sign_in_button_1.click()

job_save_btn = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button")
job_save_btn.click()

# this is for testing purposes, aimed at holding the launched window open for page inspection
# time.sleep(15)