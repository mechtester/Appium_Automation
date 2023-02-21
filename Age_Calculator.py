from appium import webdriver
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


desired_caps = {
  "platformName": "Android",
  "appium:deviceName": "7adf3fc7",
  "appium:platformVersion": "12.0",
  "appPackage": "com.happyverse.agecalculator",
  "appActivity": "com.configureit.core.MainActivity"
  }

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
wait=WebDriverWait(driver, 10)

lets = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.happyverse.agecalculator:id/BUTTON5")))
lets.click()

english = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[contains(@text,'English')]")))
english.click()

date = wait.until(EC.element_to_be_clickable((By.ID, "com.happyverse.agecalculator:id/YourName")))
date.send_keys("13-03-1996")

click_calculate=wait.until(EC.element_to_be_clickable((By.ID, "com.happyverse.agecalculator:id/BUTTON6")))
click_calculate.click()


time.sleep(2)
print(driver.current_activity)



# Wait for all elements with the class name "my-class" to be present

elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "android.widget.TextView")))
print("Element Loaded")


year = driver.find_element(By.ID,"com.happyverse.agecalculator:id/yourAge_years")
month = driver.find_element(By.ID,"com.happyverse.agecalculator:id/yourAge_month")
days = driver.find_element(By.ID,"com.happyverse.agecalculator:id/yourAge_days")

year_text = wait.until(EC.presence_of_element_located((By.ID, "com.happyverse.agecalculator:id/yourAge_years")))
print(year_text.text)

month_text = wait.until(EC.presence_of_element_located((By.ID, "com.happyverse.agecalculator:id/yourAge_month")))
print(month_text.text)

days_text = wait.until(EC.presence_of_element_located((By.ID, "com.happyverse.agecalculator:id/yourAge_days")))
print(days_text.text)

