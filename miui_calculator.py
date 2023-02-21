from appium import webdriver
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
  "platformName": "Android",
  "appium:deviceName": "7adf3fc7",
  "appium:platformVersion": "12.0",
  "appPackage": "com.miui.calculator",
  "appActivity": "com.miui.calculator.cal.CalculatorActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
time.sleep(30)

driver.find_element(AppiumBy.ID,"com.miui.calculator:id/btn_9_s").click()
driver.find_element(AppiumBy.ID,"com.miui.calculator:id/btn_1_s").click()
driver.find_element(MobileBy.ID,"com.miui.calculator:id/btn_plus_s").click()
driver.find_element(By.ID,"com.miui.calculator:id/btn_9_s").click()
driver.find_element(By.ID,"com.miui.calculator:id/btn_equal_s").click()

s=driver.find_element(By.ID,"com.miui.calculator:id/result")
print("Answer:",s.text)
