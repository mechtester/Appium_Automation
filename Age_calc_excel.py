from appium import webdriver
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from appium.webdriver.common.mobileby import MobileBy
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

# Load the workbook and get the sheet
workbook = openpyxl.load_workbook('/home/vignesh/PycharmProjects/Appium_Automation/date_data.xlsx')
sheet = workbook.active

lets = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.happyverse.agecalculator:id/BUTTON5")))
lets.click()

english = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[contains(@text,'English')]")))
english.click()

for row in sheet.iter_rows(min_row=2, values_only=True):
    Date_value = row[0]
    if Date_value is not None:
        time.sleep(3)
        date = wait.until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText")))
        date.send_keys(str(Date_value))
        time.sleep(3)

        click_calculate = wait.until(EC.element_to_be_clickable((By.ID, "com.happyverse.agecalculator:id/animation_view6")))
        click_calculate.click()

        time.sleep(3)

        year_text = wait.until(EC.presence_of_element_located((By.ID, "com.happyverse.agecalculator:id/yourAge_years")))
        print(year_text.text)

        month_text = wait.until(EC.presence_of_element_located((By.ID, "com.happyverse.agecalculator:id/yourAge_month")))
        print(month_text.text)

        days_text = wait.until(EC.presence_of_element_located((By.ID, "com.happyverse.agecalculator:id/yourAge_days")))
        print(days_text.text)

        driver.back()


